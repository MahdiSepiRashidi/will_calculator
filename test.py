from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from repository import Repository
from kivy.uix.label import Label
from kivymd.uix.list import OneLineListItem
from kivymd.uix.recycleview import RecycleView
from kivy.properties import ListProperty



repo = Repository()
class RootScreen(Screen):
    pass

class AddTaskScreen(Screen):
    def parse_and_submit(self):
            # Retrieve values from the input fields
            task_title = self.ids.task_title.text
            time_spent = self.ids.time_spent.text
            difficulty = self.ids.difficulty.text

            repo.add_task(task_title, time_spent, difficulty)
            string = str(f"task {task_title} updated to database")
            self.ids.submit_message.text = string

            # Clear the input fields after submission (optional)
            self.ids.task_title.text = ""
            self.ids.time_spent.text = ""
            self.ids.difficulty.text = "difficulty level"

class TasksScreen(Screen):
    tasks = repo.get_all_tasks()
    pass




class MyScreenManager(ScreenManager):
    pass

class TaskRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(TaskRecycleView, self).__init__(**kwargs)
        self.data = [{'text': task[1]} for task in repo.get_all_tasks()]


class MyTestApp(MDApp):
    def build(self):
        TaskRecycleView()
        return MyScreenManager()
    


if __name__ == '__main__':
    MyTestApp().run()