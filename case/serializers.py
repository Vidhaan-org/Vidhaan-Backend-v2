from rest_framework import serializers
from .models import *
from user.serializers import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ObjectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objection
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class DocumentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentDetails
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    petitioner = serializers.SerializerMethodField('get_petitioner')
    respondent = serializers.SerializerMethodField('get_respondent')
    petitioner_advocate = serializers.SerializerMethodField('get_petitioner_advocate')
    respondent_advocate = serializers.SerializerMethodField('get_respondent_advocate')
    person_involved = serializers.SerializerMethodField('get_person_involved')

    class Meta:
        model = Case
        fields = [
            "id", "cnr_number", 
            "case_type", "filing_number","filing_date", "registration_number", "registration_date",

            "first_hearing_date", "next_hearing_date", "stage_of_case", "coram", "bench", "state", "judicial", 
            
            "causelist_name","petitioner", "respondent","petitioner_advocate", "respondent_advocate", "person_involved", "under_act", "under_section", 

            "fir_state", "fir_district", "fir_police_station", "fir_number", "fir_year", 

            "category", "sub_category"
        ]


    def get_petitioner(self,instance):
        return UserSerializer(instance.petitioner, many = True).data or None

    def get_respondent(self,instance):
        return UserSerializer(instance.respondent, many = True).data or None
      
    def get_petitioner_advocate(self,instance):
        return UserSerializer(instance.petitioner_advocate, many = True).data or None
    
    def get_respondent_advocate(self,instance):
        return UserSerializer(instance.respondent_advocate, many = True).data or None

    def get_person_involved(self, instance):
        return UserSerializer(instance.person_involved, many = True).data or None