from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup: SQLite file clinic.db in your project folder
engine = create_engine('sqlite:///clinic.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Create tables (run once or whenever you update models)
def create_tables():
    Base.metadata.create_all(engine)
