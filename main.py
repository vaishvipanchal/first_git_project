from fastapi import FastAPI

from routers.router import router


app = FastAPI(
    title="Product CRUD API"
)


app.include_router(router)