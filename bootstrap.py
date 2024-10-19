"""dependency injection module"""
from database.repository import Repository
from service.task_service import TaskService
from kink import di

def inject_dependencies():
    di["repository"] = Repository()
    di["task_service"] = TaskService()
