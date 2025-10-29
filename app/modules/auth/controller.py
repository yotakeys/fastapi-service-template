from fastapi import APIRouter, Depends

from .provider import get_auth_service
from .schema import LoginRequest, TokenResponse
from .service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, service: AuthService = Depends(get_auth_service)):
    user = service.authenticate_user(request.email, request.password)
    token = service.create_token(user)
    return TokenResponse(access_token=token)
