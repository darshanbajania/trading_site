from django.db import models
from django.contrib.auth.models import User
import datetime 
from cloudinary.models import CloudinaryField

# Create your models here.

class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Profile')
    customer_id = models.CharField(default="no_id", max_length=20)
    full_name = models.CharField(default="user", max_length=100)
    email_id = models.CharField(default="user.gmail.com", max_length=100)
    address = models.CharField(default="address", max_length=500)
    purchased_product_id = models.CharField(default="[]", max_length=500)
    currently_purchased_products = models.CharField(default="{}", max_length=200)

    def __str__(self):
        return f'Customer:  {self.customer_id}'

    def save(self, *args, **kwargs):
        super().save()

class Products(models.Model):
    product_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=300)
    product_image = CloudinaryField('avatar')
    description = models.CharField(default="product description", max_length=1500)
    price = models.CharField(default='100', max_length=20)
    availability = models.CharField(default="No", max_length=10)
    product_type = models.CharField(default="NO type", max_length=100)
    stock = models.IntegerField(default="0")


    def __str__(self):
        return f'{self.product_name}'

class User_id(models.Model):
    new_user_id = models.CharField(default="user_id",max_length=15)
    total_users = models.IntegerField(default="0")

    def __str__(self):
        return f'user_id_detail'

class Purchase_details(models.Model):
    purchase_id = models.CharField(default="1", max_length=15)
    customers_purchased_id = models.CharField(default="",max_length=10)
    time_of_purchase = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    products_detail = models.CharField(default="",max_length=100)

    def __str__(self):
        return f'{self.purchase_id}'

class Home_page_images(models.Model):
    Image1 = CloudinaryField('avatar')
    Image2 = CloudinaryField('avatar')
    Image3 = CloudinaryField('avatar')

    def __str__(self):
        return f'Home page Images'

