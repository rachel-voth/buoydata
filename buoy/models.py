from django.db import models

# Create your models here.
class Buoy(models.Model):
    reading_datetime = models.DateTimeField
    wind_direction = models.IntegerField
    wind_speed = models.DecimalField
    gust = models.DecimalField
    wave_height = models.DecimalField
    dominant_period = models.DecimalField
    average_period = models.DecimalField
    mean_wave_direction = models.IntegerField
