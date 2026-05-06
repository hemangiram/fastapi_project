from fastapi import APIRouter
from app.schemas import ProductCreate
from app.services.product_service import create_product, get_products, update_product, delete_product



router = APIRouter(tags=["payments"])


@router.get("/product")
async def product():
    return {"message":"product created"}



@router.post("/products")
async def add_product(product:ProductCreate):
    return await create_product(product)




@router.get("/products")
async def list_products():
    return await get_products()




@router.put("/products/{product_id}")
async def edit_product(product_id:int, product:ProductCreate):
    return await update_product(product_id, product)




@router.delete("/products/{product_id}")
async def remove_product(product_id:int):
    return await delete_product(product_id)







