from django.urls import reverse
from rest_framework.test import APITestCase

from dish.tests.factories import DishFactory


class DishListAPITestCase(APITestCase):
    def test_get_dish_list_success(self):
        dishes = []
        for n in range(3):
            dishes.append(DishFactory())

        url = reverse('dishes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

        expected_data = {
            'id': 2,
            'name': 'Dish number 1',
            'price': 120
        }

        self.assertEqual(expected_data, response.data[1])
        
