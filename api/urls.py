from django.urls import path

from api.views import PointCreate, PointList

urlpatterns = [
    path('', PointCreate.as_view()),
    path('search/', PointList.as_view()),
]