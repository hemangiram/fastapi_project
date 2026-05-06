from app.models import Product



async def create_product(data):
    product = await Product.create(
        name = data.name,
        price = data.price
    )
    return product



async def get_products():
    return await Product.all()




async def update_product(product_id, data):
    product = await Product.get(id=product_id)

    product.name = data.name
    product.price = data.price

    await product.save()
    return product



async def delete_product(product_id):
    product = await Product.get(id=product_id)
    await product.delete()
    return {"message": "Product deleted"}