from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status


User = get_user_model()


class RegistrationAPITestCase(APITestCase):
    def setUp(self):
        # self.url = '/users/registration'
        self.url = reverse('registration')

    def test_registration_success(self):
        data = {
            'username': 'ulugbek',
            'email': 'ulugbek@gmail.com',
            'password_1': "test123",
            'password_2': "test123",
            'first_name': "Ulugbek",
            'last_name': "Kadyrbekov",
        }

        response = self.client.post(
            path=self.url,
            data=data
        )

        # status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # expected_data
        expected_data = {
            "username": "ulugbek",
            "first_name": "Ulugbek",
            "email": "ulugbek@gmail.com"
        }

        
        self.assertEqual(response.data, expected_data)
       
        # правильно ли записалось
        user = User.objects.get(username="ulugbek")
        self.assertEqual(user.username, data["username"])
        self.assertEqual(user.email, data["email"])
        self.assertEqual(user.first_name, data["first_name"])
        self.assertEqual(user.last_name, data["last_name"])

    def test_registration_different_passwords_expected_406(self):
        data = {
            'username': 'ulugbek',
            'email': 'ulugbek@gmail.com',
            'password_1': "test123",
            'password_2': "blabla777",
            'first_name': "Ulugbek",
            'last_name': "Kadyrbekov",
        }

        response = self.client.post(
            path=self.url,
            data=data
        )

        # status
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

        # expected_data
        expected_data = {"error": "Пароли не совпадают"}
        self.assertEqual(response.data, expected_data)
    
    def test_registration_missing_required_fields_expected_400(self):
        data = {
            'email': 'ulugbek@gmail.com',
            'password_1': "test123",
            'password_2': "test123",
            'first_name': "Ulugbek",
            'last_name': "Kadyrbekov",
        }

        response = self.client.post(
            path=self.url,
            data=data
        )

        # status
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # expected_data
        expected_data = {
                    "username": [
                        "This field is required."
                    ]
                }

        self.assertEqual(response.data, expected_data)

    def test_registration_invalid_email_expected_400(self):
        data = {
            'username': 'ulugbek',
            'email': 'ulugbek',
            'password_1': "test123",
            'password_2': "test123",
            'first_name': "Ulugbek",
            'last_name': "Kadyrbekov",
        }

        response = self.client.post(
            path=self.url,
            data=data
        )

        # status
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # expected_data
        expected_data = {"email": ["Enter a valid email address."]}        
        self.assertEqual(response.data, expected_data)