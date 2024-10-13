from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker


# Define the three different screens
class HomeScreen(Screen):
    pass

class AddTasksScreen(Screen):
    pass

class RecordScreen(Screen):
    def show_date_picker(self):
        date_dialog = MDDatePicker(mode="range")

        # Bind the 'on_save' method to save the chosen date range

        date_dialog.open()
        date_dialog.bind(on_save=self.on_save)



    def on_select(self, instance, value):
        # `value` is a list containing the currently selected date range
        date_range_text = ", ".join(str(date) for date in value)
        # Update the text field with the current date range selection
        print(value)

    def on_save(self, instance, value1, date_range):
        # `value` is the selected date (as datetime.date)
        self.root.ids.date_field.text = str(date_range)

# Screen Manager for handling transitions between screens
class MyScreenManager(ScreenManager):
    pass

# Define the main app class
class MyApp(MDApp):
    def build(self):
        return MyScreenManager()


        print(str(date_range))

if __name__ == '__main__':
    MyApp().run()
