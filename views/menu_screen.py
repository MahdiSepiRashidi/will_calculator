from math import sin
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from repository.repository import Repository
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import models
from kivy.app import App
from kivy_garden.graph import Graph, MeshLinePlot
Builder.load_file("views/menu_screen.kv")
repo = Repository()


class MenuScreen(Screen):
    def on_enter(self, *args):
        task_stack = self.ids.TaskStack
        tasks = repo.get_all_tasks()
        for task in tasks:
            task_instance = TaskInstance(task)

            task_stack.add_widget(task_instance)



        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                x_ticks_major=25, y_ticks_major=1,
                y_grid_label=True, x_grid_label=True, padding=5,
                x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        plot = MeshLinePlot(color=[1, 1, 1, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        graph.add_plot(plot)
        chart_view =  self.ids.ChartView
        chart_view.add_widget(graph)

        return super().on_enter(*args)

class TaskInstance(BoxLayout):
    def __init__(self, task: models.Task, **kwargs):
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

    def __init__(self, task: models.Task, **kwargs):
        super().__init__(**kwargs)
        self.task = task

    def on_release(self):
        repo.delete_task(task_id=self.task.id)
        app = App.get_running_app()
        stack_layout = app.root.get_screen("menu").ids.TaskStack
        task_instances = stack_layout.children
        for instance in task_instances:
            if instance.task.id == self.task.id:
                stack_layout.remove_widget(instance)


class AddTaskButton(Button):
    def open_add_popup(self):
        # Open the popup defined in the .kv file
        AddTaskPopup().open()


class AddTaskPopup(Popup):
    difficulty_map = {"very easy": 1,
                      "easy": 2,
                      "normal": 3,
                      "hard": 4,
                      "very hard": 5}

    def save_task(self):
        title = self.ids.TaskTitleParent.ids.TaskTitle.text
        time_spent = self.ids.TaskTimeSpentParent.ids.TaskTimeSpent.text
        # map to integer
        difficulty = self.difficulty_map[self.ids.DifficultySpinner.text]
        if self.__popup_is_empty(title, time_spent, difficulty):
            self.ids.AlertLabel.text = "please fill all fields"
            return None

        try:
            time_spent = int(time_spent)
        except ValueError:
            self.ids.AlertLabel.text = "time spent must be in numbers!"
            return None
        task = repo.add_task(title, time_spent, difficulty)
        app = App.get_running_app()
        menu_screen = app.root.get_screen('menu')
        task_instance = TaskInstance(task)
        task_stack = menu_screen.ids.TaskStack
        task_stack.add_widget(task_instance)
        self.dismiss()

    def __popup_is_empty(self, title, time_spent, difficulty):
        if title == "" or time_spent == "" or difficulty == 'difficulty level':
            return True

        return False
