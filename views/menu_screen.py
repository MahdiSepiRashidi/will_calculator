from kivy.uix.screenmanager import Screen
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from repository import Repository
Builder.load_file("views/menu_screen.kv")
repo = Repository()
class TaskStackLayout(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for task in repo.get_all_tasks():
            text = f"{task[1]} took {task[2]} minutes"
            id = task[0]
            self.add_widget(TaskElement(text, id))

class TaskElement(BoxLayout):
    def __init__(self, text, task_id, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Button(text=text))


class MenuScreen(Screen):

    def on_enter(self):
        pass
