from . import models
from rest_framework import serializers


# serializes fields in restaurant object
class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Restaurant
        fields = '__all__'


