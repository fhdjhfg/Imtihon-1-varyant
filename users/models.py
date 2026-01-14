from django.db import models
from.models import Users

# Create your models here.
class Users (models.Model):
    class role(models.TextChoices):
        SUPER_ADMIN='super_admin','Super Admin'
        ADMIN='admin','Admin'
        USER='user', 'User'
        
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    phone_number=models.IntegerChoices(default=0)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=200)
    date_of_birth=models.IntegerField(default=0)
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)

   


