from core.task_manager import TaskManager
from patterns.strategy import SortByTitle, SortByStatus


def main():
    manager = TaskManager.get_instance()

    while True:
        print("\n1. Add user\n2. Create task\n3. List tasks\n4. Change task status\n5. Change sort\n6. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            username = input("Username: ")
            manager.add_user(username)
        elif choice == "2":
            title = input("Task title: ")
            username = input("Assign to user: ")
            manager.create_task(title, username)
        elif choice == "3":
            tasks = manager.list_tasks()
            for i, t in enumerate(tasks):
                print(
                    f"{i}. {t.title} - {t.status} - assigned to {t.assigned_to.username if t.assigned_to else 'None'}")
        elif choice == "4":
            idx = int(input("Task index: "))
            new_status = input("New status (To Do/In Progress/Done): ")
            manager.change_status(idx, new_status)
        elif choice == "5":
            sort_type = input("Sort by (title/status): ")
            if sort_type == "title":
                manager.set_sort_strategy(SortByTitle())
            elif sort_type == "status":
                manager.set_sort_strategy(SortByStatus())
        elif choice == "6":
            break


if __name__ == "__main__":
    main()
