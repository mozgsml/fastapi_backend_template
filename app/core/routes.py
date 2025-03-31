from auth.routes import router as auth_router, user_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(auth_router)
router.include_router(user_router)