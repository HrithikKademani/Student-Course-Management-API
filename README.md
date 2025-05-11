
# Student Course Management API

This is a minimal REST API to manage students and their enrolled courses using FastAPI, SQLAlchemy, and PostgreSQL (or SQLite for testing).

## Features

- Add students and courses
- Enroll students in courses
- Get student details with enrolled courses
- Get course details with enrolled students

---

## Technologies Used

- **FastAPI**: Web framework
- **SQLAlchemy**: ORM for database modeling
- **Pydantic**: Data validation
- **PostgreSQL**: Backend DB (or SQLite for testing)
- **Alembic** or `Base.metadata.create_all()` for schema creation

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <project-directory>
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate       # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If using email validation:

```bash
pip install pydantic[email]
```

### 4. Set Up the Database

By default, SQLite is used. You can modify `database.py` to connect to PostgreSQL if desired.

### 5. Run the API Server

```bash
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for Swagger UI.

---

## Sample CURL Commands

### Create Student

```bash
curl -X POST http://localhost:8000/students/ \
-H "Content-Type: application/json" \
-d '{"name": "Hrithik", "email": "hrithik@example.com"}'
```

### Create Course

```bash
curl -X POST http://localhost:8000/courses/ \
-H "Content-Type: application/json" \
-d '{"title": "Python Basics", "description": "Learn Python fundamentals"}'
```

### Enroll Student

```bash
curl -X POST http://localhost:8000/enroll/ \
-H "Content-Type: application/json" \
-d '{"student_id": 1, "course_id": 1}'
```

### Get Student Details

```bash
curl http://localhost:8000/students/1
```

### Get Course Details

```bash
curl http://localhost:8000/courses/1
```

---


-

