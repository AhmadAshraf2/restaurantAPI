from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
from . import models, serializers


class ViewRestaurant(RetrieveAPIView):
    """
    Entertains GET request and returns single restaurant object
    """
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


class ViewAllRestaurant(ListAPIView):
    """
    Entertains GET request and returns all restaurant objects
    """
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


class CreateRestaurant(CreateAPIView):
    """
    Entertains POST request and creates restaurant object
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.RestaurantSerializer


class DeleteRestaurant(DestroyAPIView):
    """
    Entertains DELETE request and deletes restaurant object
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


class UpdateRestaurant(UpdateAPIView):
    """
    Entertains PUT/PATCH requests and updates existing object
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
