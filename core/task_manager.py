from typing import List, Dict
from models.task import Task
from patterns.strategy import SortStrategy, SortByTitle


class TaskManager:
    _instance = None

    def __init__(self):
        self.users: Dict[str, str] = {}
        self.tasks: List[Task] = []
        self.sort_strategy: SortStrategy = SortByTitle()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TaskManager()
        return cls._instance

    def add_user(self, username: str) -> bool:
        if username in self.users:
            return False
        self.users[username] = username
        return True

    def get_usernames(self) -> List[str]:
        return list(self.users.keys())

    def create_task(self, title: str, description: str, username: str) -> str:
        if username not in self.users:
            return "user_not_found"
        if any(task.get_title() == title for task in self.tasks):
            return "duplicate_title"
        task = Task(title, description, "To Do", assigned_to=username)
        self.tasks.append(task)
        return "success"

    def change_status(self, task: Task, new_status: str):
        task.set_status(new_status)

    def set_sort_strategy(self, strategy: SortStrategy):
        self.sort_strategy = strategy

    def list_tasks(self) -> List[Task]:
        return self.sort_strategy.sort(self.tasks)

    def delete_task(self, task: Task):
        if task in self.tasks:
            self.tasks.remove(task)
