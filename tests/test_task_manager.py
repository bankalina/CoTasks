import pytest
from core.task_manager import TaskManager
from patterns.strategy import SortByTitle, SortByStatus


@pytest.fixture
def manager():
    manager = TaskManager.get_instance()
    manager.users.clear()
    manager.tasks.clear()
    return manager


def test_add_user_success(manager):
    assert manager.add_user("alice") is True
    assert "alice" in manager.get_usernames()


def test_add_user_duplicate(manager):
    manager.add_user("bob")
    assert manager.add_user("bob") is False


def test_create_task_success(manager):
    manager.add_user("carol")
    assert manager.create_task("Task A", "Desc", "carol") is 'success'
    assert any(task.get_title() == "Task A" for task in manager.tasks)


def test_create_task_duplicate_title(manager):
    manager.add_user("carol")
    manager.create_task("Task A", "Desc", "carol")
    assert manager.create_task("Task A", "Another", "carol") is 'duplicate_title'


def test_create_task_user_not_found(manager):
    assert manager.create_task("Another Task", "No user", "ghost") is 'user_not_found'


def test_change_status(manager):
    manager.add_user("dave")
    manager.create_task("Task X", "Desc", "dave")
    task = manager.tasks[0]
    manager.change_status(task, "Done")
    assert task.get_status() == "Done"


def test_delete_task(manager):
    manager.add_user("eve")
    manager.create_task("To Delete", "Desc", "eve")
    task = manager.tasks[0]
    manager.delete_task(task)
    assert task not in manager.tasks


def test_sort_by_title(manager):
    manager.add_user("frank")
    manager.create_task("Z", "", "frank")
    manager.create_task("A", "", "frank")
    manager.set_sort_strategy(SortByTitle())
    titles = [t.get_title() for t in manager.list_tasks()]
    assert titles == ["A", "Z"]


def test_sort_by_status(manager):
    manager.add_user("grace")
    manager.create_task("Task1", "", "grace")
    manager.create_task("Task2", "", "grace")
    manager.change_status(manager.tasks[0], "In Progress")
    manager.set_sort_strategy(SortByStatus())
    statuses = [t.get_status() for t in manager.list_tasks()]
    assert statuses == sorted(statuses)
