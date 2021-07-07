from django.db import models
from core.models import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(max_length=55)
    country = models.ForeignKey(
        Country,
        models.CASCADE,
    )

    def __str__(self):
        return self.name
