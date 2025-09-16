import uuid
from fastapi import APIRouter, HTTPException
from app.crud import get_users, insert_user
from app.models.user import User

router = APIRouter(tags=["users"])

@router.get("/users")
def list_users():
    return get_users()

@router.post("/users")
def create_user(user: User):
    try:
        insert_user(user)
        return {"user_id": user.user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))