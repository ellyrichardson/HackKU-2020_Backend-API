# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# To return monitoring status
class API (models.Model):
    isMonitoring = models.BooleanField(default=False)
    isDrowsy = models.BooleanField(default=False)

# To return if sensor data should be delivered to front-end
class OnOffEndpoint (models.Model):
    turnOnConnection = models.BooleanField(default=False)

# To clear stored sensor data
class ClearSensorData (models.Model):
    clearSensorData = models.BooleanField(default=False)
