from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class TaskModel(BaseModel):
    id:int = Field(gt=0, default=1)
    title:str
    is_complete:bool = False

class UpdateTask(BaseModel):
    title:str
    is_complete:bool

task_list : List[TaskModel] = []

task_list.append(TaskModel(id=1, title="task 1", is_complete=True))
task_list.append(TaskModel(id=2, title="task 2", is_complete=False))
task_list.append(TaskModel(id=3, title="task 3", is_complete=False))
task_list.append(TaskModel(id=4, title="task 4", is_complete=False))

@app.get('/tasks')
async def get_all_tasks():
    return task_list

@app.post('/tasks')
async def create_task(new_task:TaskModel):
    task_list.append(new_task)
    return {"detail": "Task create"}
@app.get('/tasks/{task_id}')
async def get_task(task_id: int = Path(gt=0)):
    for task in task_list:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.put('/tasks/{task_id}')
async def update_task(new_task_data: UpdateTask, task_id: int = Path(gt=0)):
    for task in task_list:
        if task.id == task_id:
            task.title = new_task_data.title
            task.is_complete = new_task_data.is_complete
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int = Path(gt=0)):
    for task in task_list:
        if task.id == task_id:
            task_list.remove(task)
            return {"detail": f"Task by id={task_id} deleted"}

    raise HTTPException(status_code=404, detail="Task not found")
