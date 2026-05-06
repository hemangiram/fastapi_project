from pydantic import BaseModel



class UserCreate(BaseModel):
    username:str
    password:str


class UserOut(BaseModel):
    id:int
    username:str


class ProductCreate(BaseModel):
    name:str
    price:float


class PaymentCreate(BaseModel):
    user_id:int
    order_id:int
    amount:float
    method:str


    









