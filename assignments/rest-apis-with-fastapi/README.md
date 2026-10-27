# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for managing a task list with Python and the FastAPI framework. Practice defining request models, creating HTTP endpoints, returning JSON responses, and validating client input.

## 📝 Tasks

### 🛠️ Define the Task Model

#### Description

Complete the Pydantic model in the starter code so each task has the data needed by the API.

#### Requirements

Completed program should:

- Define a `Task` model with an integer `id`, a string `title`, and a boolean `completed` value.
- Define a `TaskCreate` model for new tasks that requires a title and defaults `completed` to `False`.
- Keep the in-memory task list available for the API endpoints.

### 🛠️ Create Collection Endpoints

#### Description

Add endpoints for listing existing tasks and creating a new task.

#### Requirements

Completed program should:

- Return all tasks as JSON from `GET /tasks`.
- Accept a new task through `POST /tasks` using the `TaskCreate` model.
- Assign each new task a unique integer ID before adding it to the task list.
- Return the newly created task from `POST /tasks` with an HTTP 201 status code.

### 🛠️ Add Task Lookup

#### Description

Add an endpoint that retrieves one task by its ID and reports a clear error when the task does not exist.

#### Requirements

Completed program should:

- Return the matching task as JSON from `GET /tasks/{task_id}`.
- Return HTTP 404 with a useful error detail when no task has the requested ID.
- Install the packages listed in `requirements.txt` before starting the server.
- Start the application with Uvicorn and make the interactive documentation available at `/docs`.
