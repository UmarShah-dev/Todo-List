from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
todo_list=[]
class Task(BaseModel):
    id: int
    title: str
    is_done:bool=False
@app.get("/tasks")
def get_tasks():
    return{"Tasks": todo_list}
@app.post("/tasks")
def create_tasks(new_tasks:Task):
    todo_list.append(new_tasks)
    return{"task":"Succesfully Added!"}
@app.put("/tasks/{task_id}")
def update_tasks(task_id:int,update_tasks:Task):
    for i in range(len(todo_list)):
        if todo_list[i].id==task_id:
            todo_list[i]=update_tasks
            return {"tasks":"task updated"}
    return {"error":"404 Not Found"}
@app.delete("/tasks/{task_id}")
def delete_tasks(task_id:int):
    for i in range(len(todo_list)):
        if todo_list[i].id==task_id:
            del todo_list[i]
            return {"Task":"deleted succesfuly"}
    return {"Error":"404 Not Found"}
