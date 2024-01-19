from fastapi import FastAPI

from .api.routers import tecnical, users

# todo прописать аннотации для свагера
app = FastAPI(
)

app.include_router(tecnical.router)
app.include_router(users.router)


# todo попробовать сделать структура проекта чуть по лучше v1 и тд (см geo-suggester)
# todo настроить линтеры в ci
# todo настроить запуск тестов с отчетом о покрытии
# todo сделать ручку metrics(prometeus)
# todo сделать ручку ready