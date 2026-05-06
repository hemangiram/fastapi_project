from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.routes.user_routes import router as user_router
from app.routes.product_routes import router as product_router
from app.routes.payment_routes import router as payment_router



app = FastAPI()


# register router
app.include_router(user_router)
app.include_router(product_router)
app.include_router(payment_router)



# Tortoise ORM setup
register_tortoise(
    app,
    db_url="postgres://root:agc123@localhost:5432/fastapi",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

