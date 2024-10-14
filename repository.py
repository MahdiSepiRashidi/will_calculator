import sqlite3
from datetime import datetime
from models import difficulty_map


class Repository:
    def __init__(self):
        
        #loading database
        self.conn = sqlite3.connect('will_calculator.db')
        # Create a cursor object
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT,
                time_spent INTEGER,
                difficulty INTEGER,
                time_created DATETIME
            )
        ''')
        self.conn.commit()
    
    def add_task(self, title, time_spent, difficulty):
        # Insert data into the table
        self.cursor.execute('''
            INSERT INTO tasks (title, time_spent, difficulty, time_created)
            VALUES (?, ?, ?, ?)
        ''', (title, time_spent, difficulty_map[difficulty], datetime.now()))

        # Commit the changes
        self.conn.commit()
    
    def get_all_tasks(self):
        self.cursor.execute('''
            SELECT * FROM tasks
        ''')

        tasks = self.cursor.fetchall()
        print(tasks)
        print()
        return tasks


