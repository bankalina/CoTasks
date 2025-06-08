import tkinter as tk
from gui.app import TaskApp
from db.database import init_db

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
