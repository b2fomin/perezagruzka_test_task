from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Point


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
        if longitude > 90 or latitude < -90:
            raise ValidationError('wrong longitude or latitude')
        return data