"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task List API")


class Task(BaseModel):
    # TODO: Add id, title, and completed fields.
    pass


class TaskCreate(BaseModel):
    # TODO: Add a required title field and a completed field that defaults to False.
    pass


# Keep the data in memory while the application is running.
tasks: list[Task] = [
    # TODO: Add at least one sample task.
]


@app.get("/tasks")
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # TODO: Create a task with the next available ID, store it, and return it.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Return the matching task or raise a 404 HTTPException.
    pass


# Install dependencies with `pip install -r requirements.txt`, then run with:
# uvicorn starter-code:app --reload
