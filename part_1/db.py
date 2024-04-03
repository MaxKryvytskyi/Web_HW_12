from sqlalchemy import create_engine, Column, String, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.config import Config


USER = Config.USER
PASSWORD = Config.PASSWORD
DB_NAME = Config.DB_NAME
DOMAIN = Config.DOMAIN
PORT = Config.PORT

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{DOMAIN}:{PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column('created_at', DateTime, default=func.now(), nullable=True)
    updated_at = Column('updated_at', DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    refresh_token = Column(String(255), nullable=True)


Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
