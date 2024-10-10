from django.db import models
from django.contrib.auth.models import User
class Houses(models.Model):
    name = models.CharField(max_length=99999999)
    image = models.ImageField(upload_to='user_recipes/')
    price = models.CharField(max_length=99999999999)
    description = models.CharField(max_length=999999)
    user_id = models.ForeignKey(User,blank=True, on_delete=models.CASCADE,related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)