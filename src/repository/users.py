from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import User
from src.schemas.user import UserSchema


async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    print(email)
    stmt = select(User).filter_by(email=email)
    user = db.execute(stmt)
    user = user.scalar_one_or_none()
    print(user.email)
    return user


async def create_user(body: UserSchema, db: Session = Depends(get_db)):
    new_user = User(**body.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: Session):
    user.refresh_token = token
    db.commit()



	

# {
#   "id": 4,
#   "username": "string1",
#   "email": "user1@example.com",
#   "password": "$2b$12$sPkdytUnbE.NXagEl32Q4u81ESpQL9/XVJ/C8zOpY42SFAQ0af.vK"
# }