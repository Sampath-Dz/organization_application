from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core_apis_server.models.models import Member
from core_apis_server.schemas.member import MemberCreate, MemberRead
from core_apis_server.crud.generic import create_item, get_all_items
from core_apis_server.models.db_factory import get_db

router = APIRouter(prefix="/members", tags=["Members"])

@router.post("/", response_model=MemberRead)
def create_member(member: MemberCreate, db: Session = Depends(get_db)):
    return create_item(db, Member, member.dict())

@router.get("/", response_model=list[MemberRead])
def read_members(db: Session = Depends(get_db)):
    return get_all_items(db, Member)
