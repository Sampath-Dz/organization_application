from fastapi import FastAPI
from .routers import router 

app = FastAPI(title="Core API Server")


app.include_router(router)
