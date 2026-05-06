from fastapi import APIRouter
from app.schemas import PaymentCreate
from app.services.payment_service import (
    create_payment,
      get_payment,
        get_payments,
          update_payment_status)

router = APIRouter(prefix="/payments", tags=["payments"])



@router.post("/")
async def add_payment(data:PaymentCreate):
    return await create_payment(data)



@router.get("/")
async def list_payments():
    return await get_payments()



@router.get("/{payment_id}")
async def single_payment(payment_id:int):
    return await get_payment(payment_id)



@router.put("/{payment_id}/status")
async def change_status(payment_id:int, status: str):
    return await update_payment_status(payment_id, status)




