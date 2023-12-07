# from datetime import datee
from pydantic import BaseModel


class Task(BaseModel):
    titulo: str
    descricao: str
    categoria: str
    data_inicio: str
    data_prevista: str


class TaskResponse(Task):
    _id: str
