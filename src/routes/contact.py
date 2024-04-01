from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.orm import Session
from datetime import date
from src.database.db import get_db
from src.schemas.contact import ContactSchema, ContactResponse, ContactDataUpdate, ContactUpdate
from src.database.models import User 
from src.repository import contact as repository_contact 
from src.services.auth import auth_service


router = APIRouter(prefix='/contacts', tags=['contacts'])

@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactSchema, db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    print(current_user.id)
    print("---------------")
    return await repository_contact.create_contact(body, db)


@router.delete("/{contact_id}", response_model=ContactResponse)
async def remove_contact(contact_id: int, db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contact.remove_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact(contact_id: int, db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contact.get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.get("/", response_model=list[ContactResponse])
async def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contact.get_contacts(skip, limit, db)
    return contacts


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(contact_id: int, body: ContactUpdate, db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contact.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.patch("/{contact_id}", response_model=ContactResponse)
async def update_data_contact(contact_id: int, body: ContactDataUpdate, db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contact.update_data_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.get("/birstdays/", response_model=list[ContactResponse])
async def get_birstdays(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contact.get_birstdays(skip, limit, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Birstday not found")
    return contacts

@router.get("/contacts/search/", response_model=list[ContactResponse])
async def search_contacts(
    first_name: str = Query(None, description="Search contacts by first name"),
    last_name: str = Query(None, description="Search contacts by last name"),
    email: str = Query(None, description="Search contacts by email"),
    phone: str = Query(None, description="Search contacts by phone"), 
    birthday: date = Query(None, description="Search contacts by birthday"),
    db: Session = Depends(get_db), 
    current_user: User = Depends(auth_service.get_current_user)): 
    contacts = await repository_contact.search_contacts(first_name, last_name, email, phone, birthday, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Birstday not found")
    return contacts