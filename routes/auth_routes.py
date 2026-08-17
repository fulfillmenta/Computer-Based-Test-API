from fastapi import APIRouter
from models.user_info import UserRegisterInfo, UserLoginInfo
from services.auth_service import register_user, login_user

router = APIRouter()


@router.post("/register")
def register(data: UserRegisterInfo):
    return register_user(data)


@router.post("/login")
def login(data: UserLoginInfo):
    return login_user(data)
