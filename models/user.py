from typing import List


class User:
    def __init__(self, username: str):
        self.username: str = username
        self.tasks: List["Task"] = []

    def notify(self, message: str) -> None:
        print(f"[Notification for {self.username}]: {message}")
