from sqlalchemy import create_engine
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


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
