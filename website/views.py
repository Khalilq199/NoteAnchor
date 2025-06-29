# this file stores standard routes for our website, anywhere users can actually go (Home page etc..)

from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

# define that this file is a blueprint for the application, it has routes inside of it

views = Blueprint("views", __name__) # setup a blueprint for the flask application

@views.route("/", methods=['GET', 'POST']) # "/" route
# this home function will be called when the "/" route is entered
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
        flash('Note deleted.', category='success')
    else:
        flash('Invalid delete attempt.', category='error')
    return redirect(url_for('views.home'))




