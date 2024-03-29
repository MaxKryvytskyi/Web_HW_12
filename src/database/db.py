import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


config = configparser.ConfigParser()
config.read("E:\Git_Files\__Python_GOIT__\__Web_2_0__\Web_HW_12\src\database\config.ini")

USER = config.get("DB", "USER")
PASSWORD = config.get("DB", "PASSWORD")
DB_NAME = config.get("DB", "DB_NAME")
DOMAIN = config.get("DB", "DOMAIN")
PORT = config.get("DB", "PORT")

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
