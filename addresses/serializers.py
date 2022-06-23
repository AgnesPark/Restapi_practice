from .models import Addresses
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ['name', 'phone_number', 'address']


