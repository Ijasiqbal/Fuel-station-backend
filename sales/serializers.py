# serializers.py
from rest_framework import serializers
from .models import Sales, ClosingSales

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class ClosingSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosingSales
        fields = '__all__'
