from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core_apis_server.models.models import Organization, Team, Member  # your models file
from core_apis_server.schemas.org import OrganizationCreate, OrganizationRead
from core_apis_server.crud.generic import create_item, get_all_items
from core_apis_server.models.db_factory import get_db

router = APIRouter(prefix="/organizations", tags=["Organizations"])

@router.post("/", response_model=OrganizationRead)
def create_org(org: OrganizationCreate, db: Session = Depends(get_db)):
    return create_item(db, Organization, org.dict())

@router.get("/", response_model=list[OrganizationRead])
def read_orgs(db: Session = Depends(get_db)):
    return get_all_items(db, Organization)
