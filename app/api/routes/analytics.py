from typing import List
from datetime import datetime

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.api.depends import get_db
from app.schemas.like import LikeGroup
from app.crud.crud_activity import read_all_likes
from app.core.exceptions import DATE_VALUE_ERROR


router = APIRouter()


@router.get('/analytics', response_model=List[LikeGroup])
def get_analytics(date_from: str, date_to: str, db: Session = Depends(get_db)):
    def convert_date(dt: str):
        try:
            converted_date = datetime.strptime(dt, '%Y-%m-%d')
        except ValueError:
            raise DATE_VALUE_ERROR
        return converted_date

    return read_all_likes(db=db, date_from=convert_date(date_from), date_to=convert_date(date_to))
