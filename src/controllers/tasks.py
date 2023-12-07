from fastapi import APIRouter, HTTPException

from src.libs.database import Database
from src.schemas.tasks import Task as TaskSchema

router = APIRouter(
    tags=['Tarefas']
)
db = Database()


@router.get('/tarefa/{id}', status_code=200)
async def read_task(id: str):
    try:
        result = db.find_task(str(id))
        print(result)
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=err)


@router.get('/tarefa', status_code=200)
async def read_all_tasks():
    try:
        result = db.find_tasks()
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=err)


@router.post('/tarefa', status_code=201)
async def create_task(payload: TaskSchema):
    try:
        result = db.create_task(payload)
        if result:
            return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=err)


@router.put('/tarefa/{id}', status_code=200)
async def update_task(id: str, payload: TaskSchema):
    try:
        result = db.update_task(str(id), payload)
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=err)


@router.delete('/tarefa/{id}', status_code=200)
async def delete_task(id: str):
    try:
        result = db.delete_task(str(id))
        return result
    except Exception as err:
        raise HTTPException(status_code=500, detail=err)
