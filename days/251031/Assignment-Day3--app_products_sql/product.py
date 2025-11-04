from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column,String,Integer,Float,create_engine
Base = declarative_base()
class Product(Base):
    __tablename__="products"
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False)
    description=Column(String(150),nullable=False)
    price=Column(Float,nullable=False)
    stock=Column(Integer,primary_key=True)
    tags=Column(String(255),nullable=False)
    def __repr__(self):
        return f"[id={self.id},name={self.name}],description={self.description},price={self.price},stock={self.stock},tags={self.tags}]"