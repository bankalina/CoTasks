from models.task import Task
from models.user import User
from typing import Optional


class TaskFactory:
    def create_task(self, title: str, assigned_to: Optional[User] = None) -> Task:
        task = Task(title, assigned_to)
        if assigned_to:
            task.attach(assigned_to)
        return task
