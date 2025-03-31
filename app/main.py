from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import init_logs
from fastapi.middleware.cors import CORSMiddleware
from app.core.routes import router

init_logs()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    pass

app = FastAPI(
    title=settings.PROJECT_NAME,
    prefix=settings.API_PREFIX,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.all_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {'status': 'ok'}

app.include_router(router, prefix=settings.API_PREFIX)