from django.contrib import admin
from .models import Customers,Products,User_id, Purchase_details, Home_page_images

# Register your models here.
admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(User_id)
admin.site.register(Purchase_details)
admin.site.register(Home_page_images)