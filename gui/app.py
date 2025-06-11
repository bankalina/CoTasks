import tkinter as tk
from tkinter import messagebox, Toplevel, ttk
from core.task_manager import TaskManager
from patterns.strategy import SortByTitle, SortByStatus


class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CoTask – Team To-Do App")

        self.manager = TaskManager.get_instance()

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        tk.Label(self.frame, text="Username").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)
        tk.Button(self.frame, text="Add User", command=self.add_user).grid(row=0, column=2)

        tk.Label(self.frame, text="Task Title").grid(row=1, column=0)
        self.task_title_entry = tk.Entry(self.frame)
        self.task_title_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Task Description").grid(row=1, column=2)
        self.task_desc_entry = tk.Entry(self.frame)
        self.task_desc_entry.grid(row=1, column=3)

        tk.Label(self.frame, text="Assign to (username)").grid(row=2, column=0)
        self.task_user_entry = tk.Entry(self.frame)
        self.task_user_entry.grid(row=2, column=1)
        tk.Button(self.frame, text="Add Task", command=self.add_task).grid(row=2, column=2)

        tk.Label(self.frame, text="New Status").grid(row=3, column=0)
        self.status_var = tk.StringVar()
        self.status_combo = ttk.Combobox(self.frame, textvariable=self.status_var)
        self.status_combo['values'] = ["To Do", "In Progress", "Done"]
        self.status_combo.grid(row=3, column=1)
        tk.Button(self.frame, text="Update Status", command=self.change_status).grid(row=3, column=2)

        tk.Button(self.frame, text="Sort by Title", command=lambda: self.set_sort("title")).grid(row=4, column=0)
        tk.Button(self.frame, text="Sort by Status", command=lambda: self.set_sort("status")).grid(row=4, column=1)
        tk.Button(self.frame, text="Refresh Tasks", command=self.load_tasks).grid(row=4, column=2)
        tk.Button(self.frame, text="Show All Tasks", command=self.show_all_tasks).grid(row=5, column=1, pady=5)

        self.task_listbox = tk.Listbox(self.root, width=60)
        self.task_listbox.pack(pady=10)

        self.task_objects = []
        self.load_tasks()

    def add_user(self):
        username = self.username_entry.get().strip()
        if username:
            success = self.manager.add_user(username)
            if success:
                messagebox.showinfo("User Added", f"User '{username}' added.")
            else:
                messagebox.showwarning("User Exists", f"User '{username}' already exists.")
            self.username_entry.delete(0, tk.END)

    def add_task(self):
        title = self.task_title_entry.get().strip()
        username = self.task_user_entry.get().strip()
        description = self.task_desc_entry.get().strip()
        if title and username:
            result = self.manager.create_task(title, description, username)
            if result == "success":
                messagebox.showinfo("Task Added", f"Task '{title}' assigned to '{username}' added.")
                self.task_title_entry.delete(0, tk.END)
                self.task_user_entry.delete(0, tk.END)
                self.task_desc_entry.delete(0, tk.END)
                self.load_tasks()
            elif result == "duplicate_title":
                messagebox.showwarning("Duplicate Task", f"A task titled '{title}' already exists.")
            elif result == "user_not_found":
                messagebox.showerror("User Not Found", f"User '{username}' does not exist.")

        else:
            messagebox.showwarning("Missing data", "Please fill in both title and username.")

    def change_status(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("No selection", "Select a task from the list.")
            return

        index = selection[0]
        selected_task = self.task_objects[index]
        new_status = self.status_var.get().strip()

        if new_status:
            self.manager.change_status(selected_task, new_status)
            messagebox.showinfo("Status Updated", f"Task '{selected_task.get_title()}' status changed to '{new_status}'.")
            self.status_var.set("")
            self.load_tasks()
        else:
            messagebox.showwarning("Missing status", "Please select a new status.")

    def set_sort(self, criteria):
        if criteria == "title":
            self.manager.set_sort_strategy(SortByTitle())
        elif criteria == "status":
            self.manager.set_sort_strategy(SortByStatus())
        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.task_objects = self.manager.list_tasks()
        for task in self.task_objects:
            self.task_listbox.insert(tk.END, task.display())

    def show_all_tasks(self):
        all_window = Toplevel(self.root)
        all_window.title("All Tasks")
        tk.Label(all_window, text="List of all tasks:", font=("Arial", 12, "bold")).pack(pady=5)
        all_list = tk.Listbox(all_window, width=70)
        all_list.pack(padx=10, pady=10)
        for task in self.task_objects:
            all_list.insert(tk.END, task.display())
