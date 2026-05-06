from fastapi import APIRouter
from app.schemas import UserCreate
from app.services.user_service import create_user, get_users




router = APIRouter()

@router.get("/")
async def home():
    return {"message":"hello user"}


@router.post("/register")
async def register(user:UserCreate):
    return await create_user(user)



@router.get("/users")
async def users():
    return await get_users()




