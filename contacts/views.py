# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render
from rest_framework import viewsets
from .models import Contacts, SMS, Call
from .serializers import ContactsSerializer, SMSSerializer, CallSerializer
from twilio.rest import Client

# Create your views here.
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    #Contacts.objects.all().delete()

class SMSViewSet(viewsets.ModelViewSet):
    queryset = SMS.objects.all()
    serializer_class = SMSSerializer

    def create(self, request):
        with open('/var/www/twillio-sid.txt', 'r') as file:
            twilio_sid = file.read().replace('\n', '')

        with open('/var/www/twillio-token.txt', 'r') as file:
            twilio_token = file.read().replace('\n', '')
            client = Client(twilio_sid, twilio_token)
            serializer = SMSSerializer(data=request.data)
            if serializer.is_valid():
                client.messages.create(
                        body=serializer.data['message'],
                        from_="+15307224633",
                        to=serializer.data['receiver'])

        return super().create(request)

class CallViewSet(viewsets.ModelViewSet):
    queryset = Call.objects.all()
    serializer_class = CallSerializer

    def create(self, request):
        with open('/var/www/twillio-sid.txt', 'r') as file:
            twilio_sid = file.read().replace('\n', '')

        with open('/var/www/twillio-token.txt', 'r') as file:
            twilio_token = file.read().replace('\n', '')
            client = Client(twilio_sid, twilio_token)
            serializer = SMSSerializer(data=request.data)
            if serializer.is_valid():
                client.calls.create(
                    twiml=serializer.data['message'],
                    from_="+15307224633",
                    to=serializer.data['receiver'])

        return super().create(request)
