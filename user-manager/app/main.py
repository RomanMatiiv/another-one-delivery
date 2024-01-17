from fastapi import FastAPI

from api.routers import tecnical, users


def create_app() -> FastAPI:
    # todo прописать аннотации для свагера
    app = FastAPI(
    )

    app.include_router(tecnical.router)
    app.include_router(users.router)

    return app
