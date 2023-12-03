from rest_framework import serializers
from .models import Professional
# from Health_Institutions.serializers import HealthSerializer
from Health_Institutions.models import HealthInstitution
class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = ('id', 'name', 'address', 'phone', 'email', 'profession', 'salary', 'speciality')

class ProfessionalsSerializer(serializers.ModelSerializer):
    institution = serializers.SerializerMethodField()
    class Meta:
        model = Professional
        fields = ('id', 'name', 'address', 'phone', 'email', 'profession', 'salary', 'speciality', 'institution')

    def get_institution(self, professional):
        from Health_Institutions.serializers import HealthSerializer
        institution = professional.hospital
        institution_serializer = HealthSerializer(institution, many=False)
        return institution_serializer.data
class ProfessionalSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = ('id', 'name', 'address', 'phone', 'email', 'profession', 'salary', 'speciality')
