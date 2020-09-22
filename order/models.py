from django.db import models

# Create your models here.
class VegProduct(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 300)
    price = models.IntegerField(default=0)
    
    image = models.ImageField(upload_to = "shop/img",default="")


    def __str__(self):
        return self.product_name


class NonVegProduct(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 300)
    price = models.IntegerField(default=0)
    
    image = models.ImageField(upload_to = "shop/img",default="")


    def __str__(self):
        return self.product_name

class VeganProduct(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 300)
    price = models.IntegerField(default=0)
    
    image = models.ImageField(upload_to = "shop/img",default="")


    def __str__(self):
        return self.product_name

class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_json = models.CharField(max_length = 2000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=7)
    contact_no = models.CharField(max_length=111)