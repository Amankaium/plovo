from django.db import models
from django.contrib.auth.models import User

from dish.models import Dish
from core.models import BaseAbstractModel


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
    email = models.EmailField(null=True, blank=False)
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


class AdditionDish(BaseAbstractModel):
    dish = models.ForeignKey(
        to=Dish,
        on_delete=models.CASCADE,
        related_name='addition_dish'
    )

    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        related_name='addition_dish'
    )

    def __str__(self):
        return self.dish.name

    class Meta:
        verbose_name = 'Доп. блюдо'
        verbose_name_plural = 'Доп. блюда'
