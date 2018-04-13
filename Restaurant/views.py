
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from . import models, serializers


class ViewRestaurant(RetrieveAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.ViewRestaurantSerializer


class CreateRestaurant(, CreateAPIView):
    serializer_class = serializers.CreateRestaurantSerializer


class DeleteRestaurant(, DestroyAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.DestroyRestaurantSerializer


class UpdateRestaurant(, UpdateAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.UpdateRestaurantSerializer
