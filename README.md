# To-Do-App-
A Django-based To-Do web app with user registration, login/logout, and CRUD task management. Tasks are grouped by date, can be marked complete, and deleted. Features a responsive UI, CSRF-protected forms, and intuitive interface for tracking daily tasks efficiently.
Perfect! 

# 📝 Django To-Do App

This is a **full-stack To-Do List web application** built using **Django**, **Python**, **HTML**, and **CSS**. It allows users to efficiently manage daily tasks with a clean and intuitive interface. The project focuses on **user authentication**, **task management**, and **organized task visualization**, making it a practical tool for personal productivity.

---

## **Features**

* **User Authentication**: Users can **register**, **log in**, and **log out** securely using Django’s built-in authentication system. Passwords are encrypted to ensure data security.
* **Task Management**: Users can **add new tasks**, **mark tasks as complete or pending**, and **delete tasks**. Each action is handled via **POST forms** with CSRF protection.
* **Task Grouping by Date**: Tasks are automatically grouped by their creation date, providing a structured overview of daily activities.
* **Responsive and Modern UI**: The app uses **flexbox-based layouts** and **CSS styling** to ensure tasks and buttons remain neatly aligned, even for long task names.
* **Dynamic Task Status**: Completed tasks are visually distinguished with green text, while pending tasks appear normally, helping users quickly identify progress.
* **Logout Functionality**: Users can safely log out with a dedicated button in the header.

---

## **Tech Stack**

* **Backend**: Django (Python framework)
* **Database**: SQLite (lightweight, file-based DB)
* **Frontend**: HTML, CSS, JavaScript
* **Authentication**: Django built-in User model and decorators
* **Version Control**: Git, GitHub

---

## **Setup & Installation**

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/django-todo-app.git
```

2. Navigate to the project folder:

```bash
cd django-todo-app
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## **Future Enhancements**

* Add task **deadlines and reminders**
* Categorize tasks by **priority or type**
* Include **user profile customization**
* Deploy the app on **Heroku / Railway / Render**

This project demonstrates **Django full-stack development**, **authentication**, **CRUD operations**, and **responsive frontend design**, making it an excellent portfolio piece for aspiring web developers.
