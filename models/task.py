from __future__ import annotations
from typing import List, Optional
from models.user import User


class Task:
    def __init__(self, title: str, assigned_to: Optional[User] = None):
        self.title: str = title
        self.status: str = "To Do"
        self.assigned_to: Optional[User] = assigned_to
        self.observers: List[User] = []

    def set_status(self, status: str) -> None:
        self.status = status
        self.notify_observers(f"Task '{self.title}' status changed to {self.status}")

    def attach(self, observer: User) -> None:
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        for observer in self.observers:
            observer.notify(message)
