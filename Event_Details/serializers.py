from rest_framework import serializers
from .models import EventDetails 

class EventDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetails
        fields = ('id', 'name', 'description', 'cotact_person', 'location', 'event_date', 'event_starttime', 'event_endtime')
    
class EventSerializer(serializers.ModelSerializer):
    institution = serializers.SerializerMethodField()
    # professionals = serializers.SerializerMethodField()
    class Meta:
        model = EventDetails
        fields = ('id', 'name', 'description', 'cotact_person', 'location', 'event_date', 'event_starttime', 'event_endtime', 'institution')

    def get_institution(self, event):
        from Health_Institutions.serializers import HealthInstitutionsSerializer
        institution = event.hospital
        institution_serializer = HealthInstitutionsSerializer(institution, many=False)
        return institution_serializer.data
class singleEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetails
        fields = ('id', 'name', 'description', 'cotact_person', 'location', 'event_date', 'event_starttime', 'event_endtime')