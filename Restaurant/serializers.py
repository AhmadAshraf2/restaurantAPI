from . import models
from rest_framework import serializers


class ViewRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Restaurant
        fields = ('name', 'opens_at', 'closes_at')


class CreateRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Restaurant
        fields = ('name', 'opens_at', 'closes_at')


class DestroyRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Restaurant
        fields = ('name', 'opens_at', 'closes_at')


class UpdateRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Restaurant
        fields = ('name', 'opens_at', 'closes_at')

