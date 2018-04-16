from . import models
from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):
    """
    serializes fields in restaurant object
    """
    class Meta:
        model = models.Restaurant
        fields = '__all__'


