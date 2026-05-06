from app.models import Payment
from app.models import User



async def create_payment(data):
    user=await User.get(id=data.user_id)


    payment=await Payment.create(
        user=user,
        order_id=data.order_id,
        amount = data.amount,
        method = data.method,
        status = "pending"
    )
    return payment