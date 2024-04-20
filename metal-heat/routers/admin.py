from typing import Annotated
from pydantic import BaseModel , Field
from sqlalchemy.orm import Session
from fastapi import APIRouter , Depends, HTTPException ,Path
from starlette import status
from models import Products
from database import SessionLocal
from .auth import get_current_user

router= APIRouter(
    prefix='/admin',
    tags=['admin']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency= Annotated[Session, Depends(get_db)]
user_dependency= Annotated[dict,Depends(get_current_user)]


@router.get("/product",status_code=status.HTTP_200_OK)
async def read_all(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail='authentication failed')
    return db.query(Products).all()


@router.delete("/product/{product_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(user:user_dependency,db:db_dependency,product_id:int=Path(gt=0)):
    if user is None or user.get('user_role') !='admin':
        raise HTTPException(status_code=401,detail='authentication failed')
    product_model=db.query(Products).filter(Products.id==product_id).first()
    if product_model is None:
        raise HTTPException(status_code=401,detail='product not found')
    db.query(Products).filter(Products.id==product_id).delete()
    db.commit()