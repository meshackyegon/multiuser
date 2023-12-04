from rest_framework.serializers import ModelSerializer
from Professional_Details.models import Professional
from Professional_Details.serializers import ProfessionalSerializer
from Event_Details.models import EventDetails
from .models import HealthInstitution
from Event_Details.serializers import EventDetailsSerializer
from rest_framework import serializers
class HealthInstitutionSerializer(ModelSerializer):
    professionals = serializers.SerializerMethodField()
    events = serializers.SerializerMethodField()
    class Meta:
        model = HealthInstitution
        fields = ('id', 'name', 'address', 'phone', 'email', 'description', 'location', 'bed_capacity', 'website', 'speciality', 'professionals', 'events')

    def get_professionals(self, obj):
        professionals = Professional.objects.filter(hospital=obj)
        professional_serializer = ProfessionalSerializer(professionals, many=True)
        return professional_serializer.data
    def get_events(self, hospital_id):
        events = EventDetails.objects.filter(hospital=hospital_id)
        event_serializer = EventDetailsSerializer(events, many=True)
        return event_serializer.data
    
class HealthInstitutionsSerializer(ModelSerializer):
    class Meta:
        model = HealthInstitution
        fields = '__all__'
    
class HealthSerializer(ModelSerializer):
    class Meta:
        model = HealthInstitution
        fields = '__all__'
class SingleHealthInstitutionSerializer(ModelSerializer):
    class Meta:
        model = HealthInstitution
        fields = ('name', 'address', 'phone', 'email', 'description', 'location', 'bed_capacity', 'website', 'speciality')
