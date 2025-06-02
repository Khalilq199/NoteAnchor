# 📝 NoteAnchor

**NoteAnchor** is a secure, full-stack note-taking web application that allows users to register, log in, and manage their personal notes. Built using **Flask**, **Python**, and **SQLite**, this project demonstrates strong backend architecture, user authentication, server-side form handling, and session management — all tied together with a clean, responsive frontend.

---

## 🚀 Features

### 🔐 User Authentication
- Secure user registration with **password hashing** (using Werkzeug)
- **Login and logout** with session management via Flask-Login
- **Input validation** and **error handling** for duplicate emails, short passwords, and missing fields
- Session cookies and login state tracking implemented via **Flask’s HTTP request–response cycle**

### 📓 Note Management (CRUD)
- Create, view, edit, and delete notes tied to each logged-in user
- Notes are stored persistently in a relational database
- Authenticated access ensures users only see and modify their own notes

### 🌐 Full-Stack Architecture
- Backend powered by **Flask** and **SQLAlchemy** ORM for database operations
- Frontend built with **HTML**, **CSS**, and templating via **Jinja2**
- Client-server communication follows the **HTTP protocol**: GET for rendering pages, POST for form submissions

### 🧠 Error Handling
- Displays user-friendly error messages for login, sign-up, and note validation failures
- Backend checks ensure empty notes are not accepted and accounts are not duplicated
- Flash messages provide real-time feedback on user actions

### 🛡️ Security Highlights
- Passwords stored securely using one-way hashing (not in plain text)
- Login-protected routes prevent unauthorized access
- CSRF-safe form handling with built-in Flask tools

