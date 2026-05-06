from tortoise import models, fields





class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=200)




class Product(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    price = fields.FloatField()



class Payment(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="payments")
    order_id = fields.IntField()
    amount = fields.FloatField()
    method = fields.CharField(max_length=50)
    status = fields.CharField(max_length=20, default="pending")








