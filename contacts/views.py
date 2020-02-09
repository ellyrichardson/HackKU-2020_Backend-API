# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render
from rest_framework import viewsets
from .models import Contacts, SMS
from .serializers import ContactsSerializer, SMSSerializer
from twilio.rest import Client

# Create your views here.
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

class SMSViewSet(viewsets.ModelViewSet):
    queryset = SMS.objects.all()
    serializer_class = SMSSerializer

    def create(self, request):
        client = Client('AC28d815fa9f39bc1392149d0f26a7c3d1', 'e9c7589d015567c7afd8ce2660b66a95')
        serializer = SMSSerializer(data=request.data)
        if serializer.is_valid():
            client.messages.create(
                    body=serializer.data['message'],
                    from_="+15307224633",
                    to=serializer.data['receiver'])

        return super().create(request)
