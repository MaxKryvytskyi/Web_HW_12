from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser

config = configparser.ConfigParser()
config.read('src/config/config.ini')

user = config.get('Security', 'USER')
password = config.get('Security', 'PASSWORD')
db_name = config.get('Security', 'DB_NAME')
domain = config.get('Security', 'DOMAIN')
port = config.get('Security', 'PORT')

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{domain}:{port}/{db_name}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
