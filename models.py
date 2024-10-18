from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    time_spent: int  # in minutes
    difficulty: int
    time_created: str
