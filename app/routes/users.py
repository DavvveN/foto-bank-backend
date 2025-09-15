from fastapi import APIRouter
from app import crud

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def create_user(name: str, email: str):
    crud.insert_user(name, email)
    return {"message": "User created"}

@router.get("/")
def list_users():
    return crud.get_users()
