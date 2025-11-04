from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column,String,Integer,Float,create_engine
Base = declarative_base()
class Employee(Base):
    __tablename__="employees"
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False)
    job_title=Column(String(150),nullable=False)
    salary=Column(Float,nullable=False)
    def __repr__(self):
        return f"[id={self.id},name={self.name}],job_title={self.job_title},salary={self.salary}]"
engine=create_engine("sqlite:///employees_db.sqlite",echo=True)#creates data base (file) if not existed
Base.metadata.create_all(engine)#creates the tables for model classes

#setup things for transactions like crud operations
SessionLocal=sessionmaker(bind=engine)
session=SessionLocal()
#crud operations
'''Lavanya=Employee(name="Lavanya",job_title="Consulting Engineer",salary=35000)
session.add(Lavanya)

Kiran=Employee(name="Kiran",job_title="Software Engineer",salary=45000)
session.add(Kiran)
session.commit()

employees=session.query(Employee).all()
print(employees)

lav=session.query(Employee).filter_by(name="Lavanya").first()
print(lav)

Lavanya.salary=38000
session.commit()

employees=session.query(Employee).all()
print(employees) '''
Lavanya = Employee(name='Lavanya', job_title='Consulting Engineer', salary=42000)
session.add(Lavanya)
session.commit()

employees = session.query(Employee).all()
print(employees)

session.delete(Lavanya)
session.commit()

employees = session.query(Employee).all()
print(employees)

