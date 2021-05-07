from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


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
