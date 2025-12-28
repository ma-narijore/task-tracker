# Task Tracker

Task Tracker is a Django-based web application designed to manage tasks and workers in a simple and structured way.  
The project demonstrates clean Django architecture, CRUD operations, and basic authentication.

---

## 🚀 Features

### ✅ Implemented

- User authentication (login / logout)
- Worker management
  - Create, update, view, and delete workers
  - Assign a position to each worker
- Task management
  - Create, update, delete tasks
  - View task list and task details
- Form validation using Django forms
- Clean UI using Django templates
- Pagination support
- Custom template tags
- SQLite database for development

---

## 🛠 Tech Stack

- Python 3
- Django
- SQLite (development database)
- HTML / CSS
- Django Template Language

---

## 📦 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ma-narijore/task-tracker.git
   cd task-tracker

2. Create and activate virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
   
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
   
4. Apply migrations:

    ```bash
    python manage.py migrate
5. Create superuser (optional):
    ```bash
    python manage.py createsuperuser
   
6. Run development server:

    ```bash
    python manage.py runserver

7. Open in browser:

    ```cpp
    http://127.0.0.1:8000/
8. 🧪 Running Tests
    ```bash
    python manage.py test