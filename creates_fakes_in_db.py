from faker import Faker
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.orm import declarative_base
from src.database.db import SessionLocal
import random
 
fake = Faker()

country_code = "+380"

Vodafone = ["50", "66", "95", "99"]	 
Kyivstar = ["67", "68", "96", "97", "98"]	
Lifecell = ["63", "73", "93"]

operator = []
operator.extend(Vodafone)
operator.extend(Lifecell)
operator.extend(Kyivstar)


def generate_fake_contacts(num: int = 10):
    Base = declarative_base()

    class Contact(Base):
        __tablename__ = "contacts"
        id = Column(Integer, primary_key=True)
        first_name = Column(String(40), nullable=False)
        last_name = Column(String(40), nullable=False)
        email = Column(String(50), nullable=False, unique=True)
        phone = Column(String(20), nullable=False, unique=True)
        birthday = Column(Date)
        data =  Column(String(250))


    db = SessionLocal()

    for _ in range(num):
        try:
            contact = Contact(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                email = fake.email(),
                phone = generate_phone_number(),
                birthday = fake.date(),
                data = fake.job())
            db.add(contact)
            db.commit()
        except Exception as err:
            db.rollback()
            print(err)
    db.close()


def generate_phone_number():
    return country_code + random.choice(operator) + ''.join(str(random.randint(0, 9)) for _ in range(7))


if __name__ == "__main__":
    generate_fake_contacts(100)