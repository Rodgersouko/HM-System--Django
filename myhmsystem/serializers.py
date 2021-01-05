from rest_framework import serializers,viewsets
from .models import *
from django.contrib.auth.hashers import make_password

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_password(password:str)->str:
        return make_password(password)
    class Meta:
        model = User
        exclude = ['user_permissions','groups']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('patient', 'description', 'date')


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('description', 'type')
