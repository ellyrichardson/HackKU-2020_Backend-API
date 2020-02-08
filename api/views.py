# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import API, OnOffEndpoint, ClearSensorData
from .serializers import APISerializer, OnOffEndpointSerializer, ClearSensorDataSerializer

class StatusAPIViewSet(viewsets.ModelViewSet):

    queryset = API.objects.all()
    serializer_class = APISerializer
    #API.objects.all().delete()

class OnOffAPIViewSet(viewsets.ModelViewSet):

    queryset = OnOffEndpoint.objects.all()
    serializer_class = OnOffEndpointSerializer

class ClearSensorDataViewSet(viewsets.ModelViewSet):

    queryset = ClearSensorData.objects.all()
    serializer_class = ClearSensorDataSerializer

    def get_queryset(self):
        API.objects.all().delete()
        return API.objects.all()
