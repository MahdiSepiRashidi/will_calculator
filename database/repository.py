import sqlite3
from datetime import date
import datetime
import models

class Repository:
    def __init__(self, ):

        # loading database
        self.conn = sqlite3.connect('database\will_calculator.db')
        # Create a cursor object
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT,
                time_spent INTEGER,
                difficulty INTEGER,
                time_created DATE,
                point INTEGER,
                FOREIGN KEY (time_spent) REFERENCES Day(date)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS days (
                date DATE PRIMARY KEY,
                point INTEGER NOT NULL,
                total_point INTEGER
                        )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS app_status (
                last_day_opened DATE
                        )
        ''')
        self.conn.commit()

    def add_task(self, title: str, time_spent: int, difficulty: int):
        # Insert data into the table
        self.cursor.execute("SELECT MAX(id) + 1 FROM tasks;")
        id = self.cursor.fetchall()[0][0]
        if id == None:
            id = 1
        task = models.Task(id=id, title=title, time_spent=time_spent,
                           difficulty=difficulty, time_created=str(date.today()))
        self.cursor.execute('''
            INSERT INTO tasks (title, time_spent, difficulty, time_created, point)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, int(time_spent), difficulty, task.time_created, task.point))

        # Commit the changes
        self.conn.commit()
        return task
    
    def get_task(self, task_id: int):
        self.cursor.execute("SELECT * FROM tasks where id = ?", (task_id,))
        task = self.cursor.fetchone()
        return models.Task(id=task[0],
                             title=task[1],
                             time_spent=task[2],
                             difficulty=task[3],
                             time_created=task[4],
                             point = task[5] )

    def get_all_tasks(self):
        self.cursor.execute('''
            SELECT * FROM tasks
        ''')

        tasks = self.cursor.fetchall()
        tasks = [models.Task(id=task[0],
                             title=task[1],
                             time_spent=task[2],
                             difficulty=task[3],
                             time_created=task[4],
                            point = task[5] ) for task in tasks]
        return tasks

    def delete_task(self, task_id: int):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()

    def restart_tasks(self):
        self.cursor.execute("DELETE FROM tasks")
        self.conn.commit()
        tasks = self.get_all_tasks()
        print()
    
    def get_last_day_opened(self):
        #gets the last day that app opened
        self.cursor.execute("SELECT last_day_opened FROM app_status")
        return self.cursor.fetchone()
    
    def update_last_day_opened(self, date_opened: date):
        self.cursor.execute("UPDATE app_status SET last_day_opened = ?", date_opened)
        self.conn.commit()
    
    def get_day(self, date_: date) -> models.Day:
        self.cursor.execute("SELECT * FROM days WHERE date= ? ", (date_,))
        day_from_db = self.cursor.fetchone()
        day = datetime.datetime.strptime(day_from_db[0], "%Y-%m-%d").date()
        day = models.Day(date=day,
                             point=day_from_db[1],
                             total_point=day_from_db[2])
        return day

    def add_day(self, date: date, point: int=0, total_point:int|None=None):
        try:
            self.cursor.execute("INSERT INTO days (date, point, total_point) VALUES (?, ?, ?)", (date, point, total_point))
        except sqlite3.IntegrityError:
            pass

        self.conn.commit()
    
    def update_day_point(self, day: date, point: int):
        self.cursor.execute("UPDATE days SET point = (point + ?) WHERE date = ?",(point, day))
