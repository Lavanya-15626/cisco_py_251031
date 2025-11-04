from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from employee import Base, Employee



engine=create_engine("sqlite:///employees_db.sqlite",echo=True)#creates data base (file) if not existed
Base.metadata.create_all(engine)#creates the tables for model classes

#setup things for transactions like crud operations
SessionLocal=sessionmaker(bind=engine)
session=SessionLocal()