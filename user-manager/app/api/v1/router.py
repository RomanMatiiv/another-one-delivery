from fastapi import APIRouter

from app.api.v1 import users

router = APIRouter(
    prefix="/v1"
)

router.include_router(users.router)
