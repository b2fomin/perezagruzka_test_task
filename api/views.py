from rest_framework.generics import CreateAPIView, ListAPIView
from django.db.models import F, ExpressionWrapper, FloatField, Func
from django.db.models.functions import ACos, Abs, Cos, Sin
from math import pi

from .models import Point
from .serializers import PointSerializer


class PointCreate(CreateAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

class PointList(ListAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

    def get_queryset(self):
        EARTH_RADIUS = 6371
        longitude = self.request.GET.get('longitude')
        latitude = self.request.GET.get('latitude')
        radius = self.request.GET.get('radius')
        if longitude is None or latitude is None or radius is None:
            return super().get_queryset()
        longitude = float(longitude)
        latitude = float(latitude)
        radius = float(radius)
        return self.queryset.annotate(dist=ACos(Sin(pi/180*F('latitude'))*Sin(pi/180*latitude)+Cos(pi/180*F('latitude'))*\
                                           Cos(pi/180*latitude)*Cos(pi/180*F('longitude')-pi/180*longitude))).filter(dist__lte=radius/EARTH_RADIUS)