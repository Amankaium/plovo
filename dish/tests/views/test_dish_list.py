from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from dish.tests.factories import DishFactory


class DishListAPITestCase(APITestCase):
    def setUp(self):
        self.url = reverse('dishes')

    def test_get_dish_list_success(self):
        dish_1 = DishFactory(name='Лагман', price=130)
        dish_2 = DishFactory()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

        expected_data_1 = {
            'id': dish_1.id,
            'name': 'Лагман',
            'price': 130
        }

        expected_data_2 = {
            'id': dish_2.id,
            'name': dish_2.name,
            'price': dish_2.price
        }

        self.assertEqual(expected_data_1, response.data[1])
        self.assertEqual(expected_data_2, response.data[0])
    
    def test_dish_list_other_methods_should_return_405(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class TestDishCreateAPITestCase(APITestCase):
    def setUp(self):
        self.data = {
            'name': 'Тестовое блюдо от шефа',
            'price': 150
        }

        self.url = reverse('create-dish')
    
    def test_create_dish_success(self):
        response = self.client.post(
            path=self.url,
            data=self.data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        expected_data = {'message': 'Блюдо успешно добавлено'}
        self.assertEqual(response.data, expected_data)
    
    def test_create_dish_via_get_405(self):
        response = self.client.get(
            path=self.url,
            data=self.data
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        expected_data = {"detail": "Method \"GET\" not allowed."}
        self.assertEqual(response.data, expected_data)
    

    def test_create_dish_without_data_400(self):
        response = self.client.post(
            path=self.url,
            data={"name": "Test"}
        )

        expected_data = {
            "price": [
                "This field is required."
            ]
        }

        self.assertEqual(response.data, expected_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
