from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from repository import Repository

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
            #TODO make text green

            # Clear the input fields after submission (optional)
            self.ids.task_title.text = ""
            self.ids.time_spent.text = ""
            self.ids.difficulty.text = "difficulty level"

class TasksScreen(Screen):
    
    def on_pre_enter(self):
        task_recycle_view = self.ids.task_recycle_view
        task_recycle_view.data = [{'text': f"{task[1]} took {task[2]} minutes"} for task in repo.get_all_tasks()]

class MyScreenManager(ScreenManager):
    pass

class MyTestApp(MDApp):
    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    MyTestApp().run()