from kink import di
class DayService:
    def __init__(self):
        self.repo = di["repository"]
    
    def update_total_points(self):
        days = self.__get_unupdated_days()
        if not days:
            return None
        for day in days:
            day.update_points()

    def __get_unupdated_days(self):
        last_day_opened = self.repo.last_date_opened()


