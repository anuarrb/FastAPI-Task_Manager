# FastAPI Task Manager

A simple REST API for managing tasks built with Python and FastAPI. This project demonstrates basic CRUD operations, request validation, HTTP exceptions, and API development using FastAPI.

## Features

- Get all tasks
- Create a new task
- Get a task by ID
- Update an existing task
- Delete a task
- Request validation using Pydantic
- HTTP error handling
- Interactive API documentation with Swagger UI

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/{task_id}` | Get a task by ID |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Task Model

```json
{
  "id": 1,
  "title": "Learn Python",
  "is_complete": false
}
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Unique task identifier |
| `title` | String | Task title |
| `is_complete` | Boolean | Task completion status |

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-task-manager.git
```

2. Navigate to the project directory:

```bash
cd fastapi-task-manager
```

3. Create a virtual environment:

```bash
python -m venv ep1-venv
```

4. Activate the virtual environment:

**Windows:**

```powershell
.\ep1-venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source ep1-venv/bin/activate
```

5. Install dependencies:

```bash
pip install "fastapi[standard]"
```

## Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

## Example

Get all tasks:

```http
GET /tasks
```

Create a task:

```http
POST /tasks
```

Request body:

```json
{
  "id": 5,
  "title": "Learn FastAPI",
  "is_complete": false
}
```

## Project Structure

```text
fastapi-task-manager/
│
├── main.py
├── ep