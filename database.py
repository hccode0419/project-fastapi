from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
import os
load_dotenv()


DB_HOST = os.environ.get("DB_HOST")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
ITEM_DB_NAME = os.environ.get("ITEM_DB_NAME")
DB_PORT = os.environ.get("DB_PORT", 3306)


SQLALCHEMY_DATABASE_URL_ITEM = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{ITEM_DB_NAME}"

item_engine = create_engine(SQLALCHEMY_DATABASE_URL_ITEM)

item_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=item_engine)

item_Base = declarative_base()

def get_itemdb():
    db = item_SessionLocal()
    try:
        yield db
    finally:
        db.close()
