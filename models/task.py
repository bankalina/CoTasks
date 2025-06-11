from typing import Optional


class Task:
    def __init__(self, title: str, description: str, status: str, assigned_to: Optional[str] = None):
        self.title = title
        self.description = description
        self.status = status
        self.assigned_to = assigned_to

    def get_title(self) -> str:
        return self.title

    def get_description(self) -> str:
        return self.description

    def get_status(self) -> str:
        return self.status

    def get_assigned_to(self) -> Optional[str]:
        return self.assigned_to

    def set_status(self, new_status: str):
        self.status = new_status

    def display(self) -> str:
        return f"{self.title} - {self.status} - {self.description} - assigned to {self.assigned_to}"
