from django.db import models

# Create your models here.
class Buoy(models.Model):
    reading_datetime = models.DateTimeField()
    wind_direction = models.IntegerField()
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    gust = models.DecimalField(max_digits=5, decimal_places=2)
    wave_height = models.DecimalField(max_digits=5, decimal_places=2)
    dominant_period = models.DecimalField(max_digits=5, decimal_places=2)
    average_period = models.DecimalField(max_digits=5, decimal_places=2)
    mean_wave_direction = models.IntegerField()
