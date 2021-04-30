from django.db import models
from django.contrib.auth.models import User

from dish.models import Dish

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    dish = models.ForeignKey(
        to=Dish,
        on_delete=models.CASCADE
    )

    location = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    discount = models.BooleanField(default=False)
    discount_sum = models.IntegerField(default=0)
    status = models.IntegerField(default=0, choices=(
        (0, 'Accepted'),
        (1, 'Completed'),
        (2, 'Canceled'),
        (3, 'Deleted'),
    ))

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'
