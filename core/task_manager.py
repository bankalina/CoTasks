from typing import Dict, List, Optional
from models.user import User
from models.task import Task
from patterns.factory import TaskFactory
from patterns.strategy import SortStrategy, SortByTitle


class TaskManager:
    _instance: Optional["TaskManager"] = None

    def __init__(self):
        self.users: Dict[str, User] = {}
        self.tasks: List[Task] = []
        self.sort_strategy: SortStrategy = SortByTitle()

    @classmethod
    def get_instance(cls) -> "TaskManager":
        if cls._instance is None:
            cls._instance = TaskManager()
        return cls._instance

    def add_user(self, username: str) -> None:
        if username not in self.users:
            self.users[username] = User(username)

    def create_task(self, title: str, username: str) -> None:
        user = self.users.get(username)
        if user:
            task = TaskFactory().create_task(title, user)
            self.tasks.append(task)
            user.tasks.append(task)

    def change_status(self, task_index: int, status: str) -> None:
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].set_status(status)

    def set_sort_strategy(self, strategy: SortStrategy) -> None:
        self.sort_strategy = strategy

    def list_tasks(self) -> List[Task]:
        return self.sort_strategy.sort(self.tasks)
