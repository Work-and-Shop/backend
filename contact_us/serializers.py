from rest_framework import serializers
from .models import *

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'



class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        fields = '__all__'
