from rest_framework import serializers
from .models import Contacts, SMS
from twilio.rest import Client

class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id', 'first_name', 'last_name', 'phone_number')

class SMSSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SMS
        fields = ('receiver', 'sender', 'message',)
