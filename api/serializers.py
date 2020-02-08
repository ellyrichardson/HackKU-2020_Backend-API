from rest_framework import serializers
from .models import API, OnOffEndpoint, ClearSensorData

# To serialize sensor monitoring status
class APISerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = API
        fields = ('isMonitoring', 'isDrowsy')

# To serialize the determination of sending data to front-end
class OnOffEndpointSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OnOffEndpoint
        fields = ('turnOnConnection',)

class ClearSensorDataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ClearSensorData
        fields = ('clearSensorData',)
