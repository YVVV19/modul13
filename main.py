from fastapi import FastAPI, Request
from datetime import datetime
from logging import getLogger, basicConfig, INFO

app = FastAPI()
logger = getLogger("middleware_logger")
basicConfig(level=INFO)


@app.middleware("/http/")
async def middleware(request: Request, call_next):
    start_time = datetime.now()
    response = await call_next(request)
#for response body/f12
    response.headers["Time-request"] = str(start_time)
    response.headers["Method"] = str(request.method)
    response.headers["URL"] = str(request.url)

#in terminal
    logger.info(f"\nЗапит: {request.method} {request.url} \nКоли був запит: {start_time}")

    return response


@app.get("/1/")
async def one():
    return {"message":"Hello"}

"""
Створіть власний middleware для FastAPI додатку, 
який буде виконувати дві основні функції: логування деталей запиту та перевірку наявності спеціального заголовка у запитах.
Розробіть middleware, який для кожного запиту логує таку інформацію: HTTP-метод, URL запиту, і час, коли запит був отриманий.
"""