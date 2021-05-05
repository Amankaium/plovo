import factory
from dish.models import Dish


class DishFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dish
    
    name = factory.Sequence(lambda n: f"Dish number {n}")
    price = factory.Sequence(lambda n: n*120)