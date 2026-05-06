from tortoise import Tortoise




async def init_db():
    await Tortoise.init(
        db_url="postgres://postgres:agc123@localhost:5432/fastapi",
        modules={
            "models": [
                "app.models.user",
                "app.models.product",
                "app.models.payment",
            ]
        }
    )

    await Tortoise.generate_schemas()