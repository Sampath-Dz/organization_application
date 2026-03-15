from fastapi import APIRouter
from .org import router as organization_router
from .team import router as team_router
from .member import router as member_router

router = APIRouter()
router.include_router(organization_router)
router.include_router(team_router)
router.include_router(member_router)
