from . import models
from rest_framework import serializers

# seperate serializsers are implemented for each CRUD operation. this is done to support scalability and abstraction.

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Restaurant
        fields = ('id', 'name', 'opens_at', 'closes_at')


class ViewRestaurantSerializer(RestaurantSerializer):
    pass


class CreateRestaurantSerializer(RestaurantSerializer):
    pass


class DestroyRestaurantSerializer(RestaurantSerializer):
    pass


class UpdateRestaurantSerializer(RestaurantSerializer):
    pass

