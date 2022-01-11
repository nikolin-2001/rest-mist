from rest_framework import serializers

from .models import PK

class PKSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PK
        fields = ('name', 'price', 'description','displei', 'processor', 'operativka', 'nakopiteli', 'ves')
