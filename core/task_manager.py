from typing import List, Dict, Optional
from models.task import Task
from db.database import add_user_to_db, add_task_to_db, get_all_tasks_from_db, update_task_status
from patterns.strategy import SortStrategy, SortByTitle
from patterns.decorator import PriorityTaskDecorator


class TaskManager:
    _instance: Optional["TaskManager"] = None

    def __init__(self):
        self.sort_strategy: SortStrategy = SortByTitle()

    @classmethod
    def get_instance(cls) -> "TaskManager":
        if cls._instance is None:
            cls._instance = TaskManager()
        return cls._instance

    def add_user(self, username: str):
        add_user_to_db(username)

    def create_task(self, title: str, description: str, username: str, priority: bool = False):
        add_task_to_db(title, description, "To Do", username)

    def change_status(self, title: str, new_status: str):
        update_task_status(title, new_status)

    def set_sort_strategy(self, strategy: SortStrategy):
        self.sort_strategy = strategy

    def list_tasks(self) -> List[Task]:
        tasks_raw = get_all_tasks_from_db()
        tasks = [Task.from_tuple(row) for row in tasks_raw]
        sorted_tasks = self.sort_strategy.sort(tasks)
        return [PriorityTaskDecorator(t) if "[PRIORITY]" in t.title else t for t in sorted_tasks]
