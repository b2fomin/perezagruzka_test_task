from django.urls import path

from api.views import PointCreate

urlpatterns = [
    path('', PointCreate.as_view()),
]