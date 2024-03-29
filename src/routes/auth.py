from fastapi import APIRouter, HTTPException, Depends, status, Query, Security
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from datetime import date
from src.database.db import get_db
from src.schemas.user import UserSchema, UserResponse, UserUpdateSchema, TokenModel
from src.repository import users as repository_users 


router = APIRouter(prefix='/users', tags=['users'])

@router.post("/signup",)
async def signup(body: UserSchema, db: Session = Depends(get_db)):
    return


@router.post("/login",)
async def signup(body: UserSchema, db: Session = Depends(get_db)):
    return


@router.get('/refresh_token',)
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security( ), db: Session = Depends(get_db)):
    return