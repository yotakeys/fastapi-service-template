from fastapi import APIRouter, Depends

from .provider import get_current_user, get_user_service
from .schema import UserCreate, UserResponse
from .service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user)


@router.get("/", response_model=list[UserResponse])
def list_users(service: UserService = Depends(get_user_service)):
    return service.list_users()


@router.get("/me", response_model=UserResponse)
def get_me(current_user=Depends(get_current_user)):
    return current_user
