# Task Management API with CLI

A simple Task Management system built using Django and Django REST Framework.
This project provides RESTful APIs to manage tasks and a CLI interface to interact with the API via terminal commands.

---

# Features

* Create, Read, Update, Delete tasks
* Mark tasks as complete/incomplete
* Assign priority to tasks
* Filter tasks by priority
* CLI tool to manage tasks from terminal
* Persistent storage using SQLite database

---

# Tech Stack

* Python 3.10+
* Django
* Django REST Framework
* Requests (for CLI API calls)
* SQLite Database

---

# Setup Instructions

### 1. Clone Repository

git clone https://github.com/yogeshkumar951/task_manager.git

### 2. Create Virtual Environment

python -m venv venv

Activate environment

venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run Migrations

python manage.py makemigrations
python manage.py migrate

### 5. Run Server

python manage.py runserver

Server will start at:

http://127.0.0.1:8000/

---

# API Endpoint Documentation

Base URL:

http://127.0.0.1:8000/api/tasks/

### Create Task

POST /api/tasks/

Request Body Example

{
"title": "Test",
"description": "Build a Test API",
"priority": "high",
"due_date": "2026-03-20"
}

---

### Get All Tasks

GET /api/tasks/

---

### Get Single Task

GET /api/tasks/{id}/

Example

GET /api/tasks/1/

---

### Update Task

PUT /api/tasks/{id}/

Example

PUT /api/tasks/1/

---

### Delete Task

DELETE /api/tasks/{id}/

---

### Filter Tasks by Priority

GET /api/tasks/?priority=high

---

# CLI Usage Examples

CLI interacts with the API using HTTP requests.

### List Tasks

python cli.py list

---

### Create Task

python cli.py create "Test" high

---

### Delete Task

python cli.py delete 1

---

### Example Output

```--------------------------------------------------
ID    Title                          Status
--------------------------------------------------
1     test                           pending
2     test1                          pending
3     test2                          pending

--------------------------------------------------```

# Assumptions Made

* SQLite database is used for simplicity.
* API server must be running before using CLI.
* Priority values allowed: low, medium, high.
* Task status values allowed: pending, complete.
* CLI interacts with the API using HTTP requests via the requests library.

