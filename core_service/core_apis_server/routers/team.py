from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core_apis_server.models.models import Team
from core_apis_server.schemas.team import TeamCreate, TeamRead
from core_apis_server.crud.generic import create_item, get_all_items
from core_apis_server.models.db_factory import get_db

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.post("/", response_model=TeamRead)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    return create_item(db, Team, team.dict())

@router.get("/", response_model=list[TeamRead])
def read_teams(db: Session = Depends(get_db)):
    return get_all_items(db, Team)
