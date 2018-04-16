from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
from . import models, serializers


# Entertains GET request and returns single restaurant object
class ViewRestaurant(RetrieveAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


# Entertains GET request and returns all restaurant objects
class ViewAllRestaurant(ListAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


# Entertains POST request and creates restaurant object
class CreateRestaurant(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.RestaurantSerializer


# Entertains DELETE request and deletes restaurant object
class DeleteRestaurant(DestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


# Entertains PUT/PATCH requests and updates existing object
class UpdateRestaurant(UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
