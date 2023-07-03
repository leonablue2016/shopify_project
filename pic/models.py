import django
import users
from django.db import models
from django.conf import settings
from django.urls import reverse




class Picture(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(default=0.00,max_digits=6, decimal_places=2)
    discounts = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pic-detail',kwargs={'pk': self.pk})

    




