# Experiment 13: Flask Student CRUD API

This experiment creates a Python Flask backend with CRUD endpoints for student data stored in a MySQL database.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Configure database environment variables (optional):

- `DB_HOST` (default: `localhost`)
- `DB_PORT` (default: `3306`)
- `DB_USER` (default: `root`)
- `DB_PASSWORD` (default: `root`)
- `DB_NAME` (default: `studentdb`)

3. Create the database if it does not exist:

```sql
CREATE DATABASE IF NOT EXISTS studentdb;
```

4. Start the server:

```bash
python app.py
```

## API Endpoints

- `GET /students` — list all students
- `GET /students/<id>` — retrieve a single student
- `POST /students` — create a new student
- `PUT /students/<id>` — update a student
- `DELETE /students/<id>` — delete a student

## Student JSON Model

```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "age": 21
}
```
