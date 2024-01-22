from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/{user_id}")
async def get_by_id(user_id: int):
    return user_id
