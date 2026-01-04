from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import Point
from .serializers import PointSerializer


class PointCreate(CreateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
