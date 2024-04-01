from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from starlette import status
from src.config.config import Config
from db import get_db, User

#     user: User = db.query(User).filter(User.email == email).first()
#     if user is None:
#         raise credentials_exception
#     return user



class Hash:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)
    
SECRET_KEY = Config.SECRET_KEY
ALGORITHM = Config.ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

async def create_access_token(data: dict, expires_delta: Optional[float]=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + timedelta(seconds=expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentils_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                         detail="Could not validate credentials", 
                                         headers={"WWW-Authenticate": "Bearer"})
    
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload["sub"]
        if email is None:
            raise credentils_exception
        
    except JWTError as err:
        raise credentils_exception
    
    user: User = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentils_exception
    return user