import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2


class Sensors(models.Model):
    sensor_id = models.CharField(max_length=100)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    img_name = models.CharField(max_length=100)
    light_data = models.IntegerField()
    battery_level = models.FloatField()

    def __str__(self):
        return self.sensor_id




