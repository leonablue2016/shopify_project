from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    money = models.DecimalField(default=0.00,max_digits=6, decimal_places=2)
    

    

