from __future__ import annotations
from typing import List


class User:
    def __init__(self, username: str):
        self.username: str = username
        self.tasks: List[Task] = []  # type: ignore

    def notify(self, message: str) -> None:
        print(f"[Notification for {self.username}]: {message}")
