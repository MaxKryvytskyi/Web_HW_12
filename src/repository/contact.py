from sqlalchemy.orm import Session
from sqlalchemy import text, func, and_
from datetime import datetime, timedelta, date

from src.database.models import Contact
from src.schemas.contact import ContactUpdate, ContactSchema, ContactDataUpdate, ContactResponse


async def create_contact(user_id: int, body: ContactSchema,  db: Session):
    contact = Contact(
        first_name = body.first_name,
        last_name = body.last_name,
        email = body.email,
        phone = body.phone,
        birthday = body.birthday,
        data = body.data,
        user_id = user_id
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def get_contacts(user_id: int, skip: int, limit: int, db: Session):
    contacts = db.query(Contact).filter(Contact.user_id==user_id).offset(skip).limit(limit).all()
    return contacts


async def get_contact(user_id: int, contact_id: int, db: Session):
    contact = db.query(Contact).filter(and_(Contact.id==contact_id, Contact.user_id==user_id)).first()
    return contact


async def remove_contact(user_id: int, contact_id: int, db: Session):
    contact = db.query(Contact).filter(and_(Contact.id==contact_id, Contact.user_id==user_id)).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(user_id: int, contact_id: int, body: ContactUpdate, db: Session):
    contact = db.query(Contact).filter(and_(Contact.id==contact_id, Contact.user_id==user_id)).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.data = body.data
        db.commit()
    return contact


async def update_data_contact(user_id: int, contact_id: int, body: ContactDataUpdate, db: Session):
    contact = db.query(Contact).filter(and_(Contact.user_id==user_id, Contact.id==contact_id)).first()
    if contact:
        contact.data = body.data
        db.commit()
    return contact


async def get_birstdays(user_id: int, skip: int, limit: int, db: Session):
    today = datetime.today()
    seven_days_later = today + timedelta(days=7)
    contact_birthdays = db.query(Contact).filter(and_(Contact.user_id==user_id,
        text("TO_CHAR(birthday, 'MM-DD') BETWEEN :start_date AND :end_date")).params(
        start_date=today.strftime('%m-%d'), 
        end_date=seven_days_later.strftime('%m-%d'))).offset(skip).limit(limit).all()
    contact_list = []
    
    for contact in contact_birthdays:
        contact_response = ContactResponse(
            id=contact.id,
            first_name=contact.first_name,
            last_name=contact.last_name,
            email=contact.email,
            phone=contact.phone,
            birthday=contact.birthday,
            data=contact.data,
            user_id=contact.user_id)
        contact_list.append(contact_response)
    return contact_list


async def search_contacts(user_id: int, first_name: str, last_name: str, email: str, phone: str, birthday: date, db: Session):
    query = db.query(Contact).filter(and_(Contact.user_id==user_id))
 
    contacts = []
    if first_name:
        query1 = query.filter(Contact.first_name.ilike(f"%{first_name}%"))
        contacts.extend(query1.all())
    if last_name:
        query1 = query.filter(Contact.last_name.ilike(f"%{last_name}%"))
        contacts.extend(query1.all())
    if email:
        query1 = query.filter(Contact.email.ilike(f"%{email}%"))     
        contacts.extend(query1.all())
    if phone:
        query1 = query.filter(Contact.phone.ilike(f"%{phone}%"))       
        contacts.extend(query1.all())
    if birthday:
        query1 = query.filter(func.DATE(Contact.birthday) == birthday)
        contacts.extend(query1.all())
 
    return list(set(contacts))
