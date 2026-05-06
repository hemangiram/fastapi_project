from app.models import User
from passlib.context import CryptContext




pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)



async def create_user(data):
    print("start hashing")

    hashed_password = pwd_context.hash(data.password)

    print("hashed:", hashed_password)

    user = await User.create(
        username=data.username,
        password=hashed_password
    )

    print("user created")

    return user


async def get_users():
    return await User.all()

