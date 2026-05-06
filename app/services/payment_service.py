from app.models import Payment
from app.models import User
from tortoise.exceptions import DoesNotExist



async def create_payment(data):
    try:
        user = await User.get(id=data.user_id)
    except DoesNotExist:
        return {"error":"user not found"}
    
    payment=await Payment.create(
        user=user,
        order_id = data.order_id,
        amount = data.amount,
        method = data.method,
        status = "pending"
    )
    return payment




async def get_payments():
    return await Payment.all()



async def get_payment(payment_id: int):
    return await Payment.get(id = payment_id)




async def update_payment_status(payment_id: int, status: str):
    payment = await Payment.get(id=payment_id)
    payment.status = status
    await payment.save()
    return payment


