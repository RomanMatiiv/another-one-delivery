from fastapi import APIRouter

from app.api.v1.users import users

router = APIRouter(
    prefix="/v1"
)

router.include_router(users.router)
