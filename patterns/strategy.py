from abc import ABC, abstractmethod
from typing import List
from models.task import Task


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, tasks: List[Task]) -> List[Task]:
        pass


class SortByTitle(SortStrategy):
    def sort(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks, key=lambda t: t.title)


class SortByStatus(SortStrategy):
    def sort(self, tasks: List[Task]) -> List[Task]:
        order = {"To Do": 0, "In Progress": 1, "Done": 2}
        return sorted(tasks, key=lambda t: order.get(t.get_status(), 99))

