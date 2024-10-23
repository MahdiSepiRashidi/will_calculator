from kink import di
from datetime import date, timedelta
from models import Task
from typing import List
class DayService:
    def __init__(self):
        self.repo = di["repository"]
    
    def update_total_points(self):
        days = self.__get_unupdated_days()
        if not days:
            return None
        for day in days:
            day.update_points()
    
    def create_new_day(self):
        last_day_opened = self.repo.get_last_date_opened()
        if last_day_opened == date.today():
            return None
        return self.repo.add_day(date.today())

    def __get_unupdated_days(self) ->List[Task]|None:
        last_day_opened = self.repo.get_last_date_opened()
        if last_day_opened == date.today():
            return None
        return self.__get_dates_between(last_day_opened, date.today()) 
    
    def __get_dates_between(self, date1, date2):
        dates = []
        days = []
        current_date = date1
        while current_date <= date2:
            current_date += timedelta(days=1)
            dates.append(current_date)
        
        for date in dates:
            days.append(self.repo.get_day(date))
            
        return days

        
        


