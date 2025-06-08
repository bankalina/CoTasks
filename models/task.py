from typing import Optional


class Task:
    def __init__(self, title: str, status: str, assigned_to: Optional[str] = None):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    @classmethod
    def from_tuple(cls, row: tuple) -> "Task":
        return cls(title=row[0], status=row[1], assigned_to=row[2])

    def display(self) -> str:
        return f"{self.title} - {self.status} - assigned to {self.assigned_to}"
