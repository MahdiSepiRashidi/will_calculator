from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from views.menu_screen import MenuScreen

class MyScreenManager(ScreenManager):
    pass

class WillCalculatorApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        return sm

if __name__ == '__main__':
    WillCalculatorApp().run()