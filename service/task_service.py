from math import sin
from kivy.uix.stacklayout import StackLayout
from models import TaskInstance, Task
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.uix.label import Label
from kink import inject
from kink import di

import models


@inject 
class TaskService:
    def __init__(self):
        self.repo = di["repository"]

    def fill_task_view(self, task_stack: StackLayout):
        tasks = self.repo.get_all_tasks()
        for task in tasks:
            task_instance = TaskInstance(task)

            task_stack.add_widget(task_instance)
    
    def fill_graph(self, chart_view: BoxLayout):
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                x_ticks_major=25, y_ticks_major=1,
                y_grid_label=True, x_grid_label=True, padding=5,
                x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        plot = MeshLinePlot(color=[1, 1, 1, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        graph.add_plot(plot)
        chart_view.add_widget(graph)

    def delete_task(self, task: Task):
        self.repo.delete_task(task_id=task.id)
        app = App.get_running_app()
        stack_layout = app.root.get_screen("menu").ids.TaskStack
        task_instances = stack_layout.children
        for instance in task_instances:
            if instance.task.id == task.id:
                stack_layout.remove_widget(instance)
    
    def save_task(self, title: str, time_spent: str, difficulty: str, AlertLabel: Label):
        if self.__popup_is_empty(title, time_spent, difficulty):
            AlertLabel.text = "please fill all fields"
            return None

        try:
            time_spent = int(time_spent)
        except ValueError:
            AlertLabel.text = "time spent must be in numbers!"
            return None
        task = self.repo.add_task(title, time_spent, difficulty)
        self.repo.update_day_point(task.time_created, task.point)
        app = App.get_running_app()
        menu_screen = app.root.get_screen('menu')
        task_instance = models.TaskInstance(task)
        task_stack = menu_screen.ids.TaskStack
        task_stack.add_widget(task_instance)
        

    def __popup_is_empty(self, title, time_spent, difficulty):
        if title == "" or time_spent == "" or difficulty == 'difficulty level':
            return True

        return False