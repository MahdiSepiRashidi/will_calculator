from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from database.repository import Repository
from kivy.lang import Builder
from kink import di
Builder.load_file("views/menu_screen.kv")
repo = Repository()


class MenuScreen(Screen):
    def on_enter(self, *args):
        task_service = di["task_service"]
        task_service.fill_graph(self.ids.ChartView)
        task_service.fill_task_view(self.ids.TaskStack)
        

        return super().on_enter(*args)


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
        task_service = di["task_service"]

        title = self.ids.TaskTitleParent.ids.TaskTitle.text
        time_spent = self.ids.TaskTimeSpentParent.ids.TaskTimeSpent.text
        # map to integer
        difficulty = self.difficulty_map[self.ids.DifficultySpinner.text]
        AlertLabel = self.ids.AlertLabel
        task_service.save_task(title, time_spent, difficulty, AlertLabel)
        self.dismiss()
