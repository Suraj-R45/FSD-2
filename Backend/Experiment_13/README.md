# Experiment 13: Flask Student CRUD API

This experiment creates a Python Flask backend with CRUD endpoints for student data stored in a MySQL database.

## Learning Outcomes

- Understand how to connect a Flask application to a MySQL database.
- Build RESTful CRUD endpoints for creating, reading, updating, and deleting student records.
- Design and use a `student` table schema to store student information.
- Handle JSON request/response payloads in Flask routes.
- Verify database persistence and API flow with MySQL-backed operations.


. Create the database if it does not exist:

```sql
CREATE DATABASE IF NOT EXISTS studentdb;
```



## API Endpoints

- `GET /students` — list all students
- `GET /students/<id>` — retrieve a single student
- `POST /students` — create a new student
- `PUT /students/<id>` — update a student
- `DELETE /students/<id>` — delete a student


