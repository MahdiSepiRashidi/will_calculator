from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from views.menu_screen import MenuScreen
from bootstrap import inject_dependencies, di

inject_dependencies()
class MyScreenManager(ScreenManager):
    pass

class WillCalculatorApp(App):
    def build(self):
        self.day_service = di["day_service"]

        sm = MyScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        return sm
    
    def on_start(self):
        
        self.day_service.create_new_day()
        self.day_service.update_total_points()
        return super().on_start()

if __name__ == '__main__':
    WillCalculatorApp().run()