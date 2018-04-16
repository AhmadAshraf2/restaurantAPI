from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import User, Restaurant


class AccountTests(APITestCase):

    # creates user and objects in Django test Database
    def setUp(self):
        Restaurant.objects.create(
            name='testname', closes_at="12:00:00", opens_at="12:00:00"
        )

        User.objects.create(
            username='django_test', password='abc123456', email='django_test@example.com',
            is_superuser=True, is_staff=True
        )

    def test_1create_restaurant_with_credentials(self):
        token = Token.objects.get(user__username='django_test')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('create_restaurant')
        data = {'name': 'gaya', 'opens_at': '12:00:00', 'closes_at': '12:00:00'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_2create_restaurant_without_credentials(self):
        url = reverse('create_restaurant')
        data = {'name': 'xyz', 'opens_at': '12:00:00', 'closes_at': '12:00:00'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_3view_restaurant(self):
        restaurant = Restaurant.objects.get(name='testname')
        url = reverse('view_restaurant', args=[restaurant.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_4update_restaurant(self):
        token = Token.objects.get(user__username='django_test')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        restaurant = Restaurant.objects.get(name='testname')
        url = reverse('update_restaurant', args=[restaurant.id])
        data = {'name': 'updated_name', 'opens_at': '12:00:00', 'closes_at': '12:00:00'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_5delete_restaurant(self):
        token = Token.objects.get(user__username='django_test')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        restaurant = Restaurant.objects.get(name='testname')
        url = reverse('delete_restaurant', args=[restaurant.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
