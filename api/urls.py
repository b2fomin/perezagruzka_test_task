from django.urls import path

from api.views import PointCreate, PointList, MessageCreate, MessageList

urlpatterns = [
    path('', PointCreate.as_view()),
    path('search/', PointList.as_view()),
    path('messages/', MessageCreate.as_view()),
    path('search/messages/', MessageList.as_view()),
]