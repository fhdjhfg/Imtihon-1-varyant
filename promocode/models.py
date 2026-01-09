from django.db import models
from.models import Promocode

# Create your models here.
class Promocode (models.Model):
    name=models.CharField(max_length=100)
    limit_max_user=models.IntegerField(default=0)
    is_expired = models.BooleanField(default=True)
    current_price = models.IntegerField(default=0)
    created_by = models.ForeignKey( on_delete=models.CASCADE)
    updated_by = models.ForeignKey(on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
