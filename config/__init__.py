from contextlib import contextmanager
from .connection import engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


@contextmanager
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


Base = declarative_base(bind=engine)
metadata = Base.metadata
