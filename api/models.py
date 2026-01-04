from django.db import models

class Point(models.Model):
    name = models.CharField(max_length=50, unique=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

class Message(models.Model):
    message = models.TextField(max_length=500)
    point = models.ForeignKey(Point, on_delete=models.CASCADE)