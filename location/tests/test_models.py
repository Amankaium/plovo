from rest_framework.test import APITestCase
from location.models import City, Country


class CountryTestCase(APITestCase):
    def test_create_country_success(self):
        country = Country(name="Test Country")
        country.save()
        self.assertEqual(country.name, "Test Country")


class CityModelTestCase(APITestCase):
    def test_create_city_success(self):
        country = Country(name="Test Country")
        country.save()

        city = City(name="Test City A", country=country)
        city.save()

        self.assertEqual(city.name, "Test City A")
        self.assertEqual(city.country, country)
        self.assertEqual(city.country.name, "Test Country")