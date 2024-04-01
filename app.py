from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
import uvicorn

from auth import create_access_token, get_current_user, Hash
from db import User, get_db

app = FastAPI()
hash_handler = Hash()


class UserModel(BaseModel):
    username: str
    email: EmailStr
    password: str



@app.post("/signup")
async def singop(body: UserModel, db: Session = Depends(get_db)):
    exist_user = db.query(User).filter(User.email == body.email, User.username == body.username).first()

    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    
    new_user = User(username=body.username, email=body.email, password=hash_handler.get_password_hash(body.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {'username': new_user.username , "user_email": new_user.email}










if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)