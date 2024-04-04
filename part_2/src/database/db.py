import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read('src/config/config.ini')

user = config.get('DB', 'user')
password = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')
port = config.get('DB', 'port')


engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{domain}:{port}/{db_name}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()