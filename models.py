from pydantic import BaseModel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kink import di

class Task(BaseModel):
    id: int
    title: str
    time_spent: int  # in minutes
    difficulty: int
    time_created: str

class TaskInstance(BoxLayout):
    
    def __init__(self, task: Task, **kwargs):
        super().__init__(**kwargs)
        self.task = task
        self.size_hint = (1, None)
        self.height = "40dp"
        self.add_widget(Button(
            text=f'text: {task.title} took {task.time_spent} minutes in {task.time_created}'))
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


