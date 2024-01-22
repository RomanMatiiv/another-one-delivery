from fastapi import APIRouter

router = APIRouter(
    prefix="/technical",
    tags=["technical"],
)


@router.get("/ping")
async def ping():
    return "pong"


@router.get("/ready")
async def ready():
    raise NotImplementedError


@router.get("/metrics")
async def metrics():
    raise NotImplementedError