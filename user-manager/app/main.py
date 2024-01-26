from fastapi import FastAPI

from .api import tecnical
from .api.v1 import router as router_v1

# todo прописать аннотации для свагера
app = FastAPI()

app.include_router(tecnical.router)
app.include_router(router_v1.router)

# todo сделать ручку metrics(prometeus)
# todo сделать ручку ready
# todo настроить запуск статических анализаторов mypy и pyright
# todo настроить запуск тестов и линтера в ci
# todo разобраться с ошибкой вывода make "make: *** [test] Error"