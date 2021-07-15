from fastapi import FastAPI, Depends
from database import Session
from tables import User, Item
import api
import json
import models
from sqlalchemy.orm import load_only
from passlib.hash import bcrypt
from services.auth import AuthService, get_current_user
from services.operations import OperationsService
from datetime import date 

app = FastAPI(
    title='Accountr',
    description='retail management',
    version='1.0.0',
)


@app.get("/")
async def root():
    return {"message": "connect to fast api successfully"}

@app.get("/users")
async def get_users():
    user_infor = Session().query(User).all()
    user_infor = [x.__dict__ for x in user_infor]
    user_infor = [{"username": x["username"], "email": x["email"], "id": x["id"]} for x in user_infor]
    return {"message": user_infor}

@app.get("/getid")
async def get_id(username):
    return Session().query(User).filter(User.username == username).options(load_only("id")).first()

@app.post("/item")
async def set_item(ids, kind, amount, operations_service: OperationsService = Depends()):
    today = date.today()
    operation_data = models.OperationCreate(
        date=today,
        kind=kind,
        amount=int(amount)
    )
    return operations_service.create(
        ids, operation_data
    )

@app.get("/items")
async def get_items(id, operations_service: OperationsService = Depends()):

    results = operations_service.get_many(id)
    results = [x.__dict__ for x in results]
    results = [{
        "date": x["date"],
        "kind": x["kind"],
        "amount": x["amount"]
        }for x in results]
    #print(results)
    return {"message": results}

@app.post("/checkuser")
async def check_user(username: str):
    usernames_id = Session().query(User).options(load_only("username")).all()
    usernames = [x.__dict__["username"] for x in usernames_id]
    #print(usernames)
    return {"message": username in usernames}

@app.post("/register")
async def register(username: str, password: str, email: str, auth_service: AuthService = Depends()):
    user = models.UserCreate(
        email=email,
        username=username,
        password=bcrypt.hash(password),
        priority=1
    )
    return auth_service.register_new_user(user)
    return {"message": True}

app.include_router(api.router)
