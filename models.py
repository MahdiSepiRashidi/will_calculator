from pydantic import BaseModel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kink import di
from kivy.properties import StringProperty
from datetime import date, timedelta

class Task:
    def __init__(self, id, title, time_spent, difficulty, time_created, point: int=None):
        #TODO: able to add tasks that have no time_spent
        self.id = id
        self.title = title
        self.time_spent = time_spent  # in minutes
        self.difficulty = difficulty
        self.time_created = time_created
        self.point = self.__calculate_points()

    def __calculate_points(self):
        return self.difficulty * self.time_spent

class TaskInstance(BoxLayout):
    
    def __init__(self, task: Task, **kwargs):
        super().__init__(**kwargs)
        self.task = task
        self.size_hint = (1, None)
        self.height = "40dp"
        self.add_widget(Button(
            text=f'text: {task.title} with {task.point} pts took {task.time_spent} minutes in {task.time_created}'))
        self.add_widget(TaskDeleteButton(task))

class TaskDeleteButton(Button):
    text = "delete"
    size_hint = (0.1, 1)
    background_color = (0.5, 0, 0, 1)

    def __init__(self, task: Task, **kwargs):
        super().__init__(**kwargs)
        self.task = task
        self.task_service = di["task_service"]

    def on_release(self):
        self.task_service.delete_task(self.task)

class ShowGraphButton(Button):
    year = StringProperty()
    month = StringProperty()
    def on_release(self):
        if not self.data_is_valid():
            return None
        print(self.year, self.month)
        return super().on_release()
    
    def data_is_valid(self):
        if self.year =="year" or self.month == "month":
            return False
        return True

class Day:
    def __init__(self, date: date, tasks: list=[], point: int=0, total_point :int|None=None):
        self.date = date
        self.tasks = tasks
        self.point = point # the point gathered in day
        self.total_point = total_point # total will point
        self.repo = di["repository"]
    
    def update_points(self):
        if self.total_point == 0:
            return None
        yesterday = self.repo.get_day(self.date - timedelta(days=1))
        self.total_point = yesterday.total_point + self.point - yesterday.total_point/6


