from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from . import models, serializers


class ViewRestaurant(RetrieveAPIView):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.ViewRestaurantSerializer


class CreateRestaurant(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CreateRestaurantSerializer


class DeleteRestaurant(DestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.DestroyRestaurantSerializer


class UpdateRestaurant(UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.UpdateRestaurantSerializer
