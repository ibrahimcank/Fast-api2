from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean


class Users(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, index=True)
    username= Column(String,unique=True)
    first_name=Column(String)
    last_name=Column(String)
    hashed_password=Column(String)
    role=Column(String)



class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    client = Column(String)
    operation = Column(String)
    tempature = Column(Integer)
    process = Column(String)
    kilogram= Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id=Column(Integer,ForeignKey("users.id"))

