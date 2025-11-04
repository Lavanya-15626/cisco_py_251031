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
engine=create_engine("sqlite:///employees_db.sqlite",echo=True)#creates data base (file) if not existed
Base.metadata.create_all(engine)#creates the tables for model classes

#setup things for transactions like crud operations
SessionLocal=sessionmaker(bind=engine)
session=SessionLocal()
#crud operations
SmartWatch=Product(name="SmartWatch",description="Water-resistant smartwatch with heart rate and step counter",price=35000,stock=45,tags="electronics,health,wearables,fitness")
session.add(SmartWatch)

portable_power_bank=Product(name="portable power bank",description="fast charging power bank with dual USB ports and LED indicator",price=1500,stock=60,tags="electronics,charger,portable")
session.add(portable_power_bank)
session.commit()

wireless_bluetooth_headphones=Product(name="wireless bluetooth headphones",description="wireless bluetooth headphones with deep bass and 20-hr battery life",price=2500,stock=40,tags="electronics,audio,headphones")
session.add(wireless_bluetooth_headphones)
employees=session.query(Product).all()
print(employees)

Smart=session.query(Product).filter_by(name="SmartWatch").first()
print(Smart)

SmartWatch.price=5000
session.commit()


session.delete(wireless_bluetooth_headphones)
session.commit()

products = session.query(Product).all()
print(products)
