from kivy.uix.stacklayout import StackLayout
from models import TaskInstance, Task
from kivy.app import App
from kink import inject
from kink import di


@inject 
class TaskService:
    def __init__(self):
        self.repo = di["repository"]

    def fill_task_view(self, task_stack: StackLayout):
        tasks = self.repo.get_all_tasks()
        for task in tasks:
            task_instance = TaskInstance(task)

            task_stack.add_widget(task_instance)

    def delete_task(self, task: Task):
        self.repo.delete_task(task_id=task.id)
        app = App.get_running_app()
        stack_layout = app.root.get_screen("menu").ids.TaskStack
        task_instances = stack_layout.children
        for instance in task_instances:
            if instance.task.id == task.id:
                stack_layout.remove_widget(instance)