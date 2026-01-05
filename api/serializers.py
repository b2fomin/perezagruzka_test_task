from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Point, Message


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = [
            'name',
            'longitude',
            'latitude',
        ]

    def validate(self, data):
        longitude = data['longitude']
        latitude = data['latitude']
        if longitude > 90 or longitude < -90 or latitude > 180 or latitude < -180:
            raise ValidationError('wrong longitude or latitude')
        return data

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'point',
            'message'
        ]