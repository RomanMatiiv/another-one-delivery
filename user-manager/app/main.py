from fastapi import FastAPI

from .api import tecnical
from .api.v1 import router as router_v1

# todo прописать аннотации для свагера
app = FastAPI()

app.include_router(tecnical.router)
app.include_router(router_v1.router)

# todo настроить запуск тестов с отчетом о покрытии
# todo сделать ручку metrics(prometeus)
# todo сделать ручку ready
