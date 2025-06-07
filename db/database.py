import sqlite3


def init_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT NOT NULL,
            assigned_to TEXT,
            FOREIGN KEY (assigned_to) REFERENCES users(username)
        )
    ''')
    conn.commit()
    conn.close()


def add_user_to_db(username: str):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", (username,))
    conn.commit()
    conn.close()


def add_task_to_db(title: str, status: str, username: str):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, status, assigned_to) VALUES (?, ?, ?)", (title, status, username))
    conn.commit()
    conn.close()


def get_all_tasks_from_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, status, assigned_to FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def update_task_status(title: str, new_status: str):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE title = ?", (new_status, title))
    conn.commit()
    conn.close()
