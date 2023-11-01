from rest_framework import serializers
from .models import Visit, Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name')


class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = '__all__'
        read_only_fields = ('id', 'date_created')
        extra_kwargs = {
            'store': {'write_only': True},
            'latitude': {'write_only': True},
            'longitude': {'write_only': True},
        }
