from rest_framework import serializers
from .models import * 

class UserSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = CustomUser 
        fields = ["mobile", "email", "first_name", "last_name"]

class UserDetailsSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField('get_gender')
    pin = serializers.SerializerMethodField('get_pin')
    address = serializers.SerializerMethodField('get_address')
    city = serializers.SerializerMethodField('get_city')
    district = serializers.SerializerMethodField('get_district')
    state = serializers.SerializerMethodField('get_state')
    country = serializers.SerializerMethodField('get_country')

    class Meta: 
        model = CustomUser 
        fields = ["mobile", "email", "first_name", "last_name", "gender", "pin", "address", "city", "district", "state", "country"]

    def get_gender(self, instance):
        return UserDetails.objects.get(user = instance).gender 

    def get_pin(self, instance):
        return UserDetails.objects.get(user = instance).pin 

    def get_address(self, instance):
        return UserDetails.objects.get(user = instance).address 

    def get_city(self, instance):
        return UserDetails.objects.get(user = instance).city 

    def get_district(self, instance):
        return UserDetails.objects.get(user = instance).district 

    def get_state(self, instance):
        return UserDetails.objects.get(user = instance).state 

    def get_country(self, instance):
        return UserDetails.objects.get(user = instance).country 
