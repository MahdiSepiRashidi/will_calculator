"""dependency injection module"""
from database.repository import Repository
from service.task_service import TaskService
from service.day_service import DayService
from kink import di

def inject_dependencies():
    di["repository"] = Repository()
    di["task_service"] = TaskService()
    di["day_service"] = DayService()
