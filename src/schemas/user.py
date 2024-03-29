from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=12)
    avatar: str = Field(min_length=3, max_length=40) 


class UserUpdateSchema(UserSchema):
    username: str
    email: EmailStr
    password: str 
    avatar: str  


class UserResponse(BaseModel):
    id: int 
    username: str
    email: str 
    password: str 
    avatar: str  

    class Config:
        from_attributes = True
        # orm_mode = True


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
