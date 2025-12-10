from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.schemas import TaskCreate, TaskResponse, TaskBase
from app.controller import *

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo FastAPI")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tasks", response_model=list[TaskResponse])
def listar(db: Session = Depends(get_db)):
    return list_tasks(db)

@app.post("/tasks", response_model=TaskResponse)
def criar(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(task, db)

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def buscar(task_id: int, db: Session = Depends(get_db)):
    task = buscar_tarefa(task_id, db)
    if not task:
        raise HTTPException(404, "Tarefa não encontrada")
    return task

@app.put("/tasks/{task_id}", response_model=TaskResponse)
def atualizar(task_id: int, task: TaskBase, db: Session = Depends(get_db)):
    updated = update_task(task_id, task, db)
    if not updated:
        raise HTTPException(404, "Não encontrada")
    return updated

@app.delete("/tasks/{task_id}")
def deletar(task_id: int, db: Session = Depends(get_db)):
    deleted = delete_task(task_id, db)
    if not deleted:
        raise HTTPException(404, "Não encontrada")
    return {"msg": "Removida com sucesso!"}