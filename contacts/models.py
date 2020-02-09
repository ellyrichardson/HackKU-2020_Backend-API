# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contacts (models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.phone_number

class SMS (models.Model):
    receiver = models.CharField(max_length=225)
    sender = models.CharField(max_length=225)
    message = models.CharField(max_length=225)

    def __str__(self):
        return self.message

class Call (models.Model):
    receiver = models.CharField(max_length=225)
    sender = models.CharField(max_length=225)
    message = models.CharField(max_length=225)

    def __str__(self):
        return self.message
