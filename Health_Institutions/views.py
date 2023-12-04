from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HealthInstitution
from .serializers import HealthInstitutionSerializer, SingleHealthInstitutionSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

@api_view(['GET'])
def health_institution_list(request):
    health_institutions = HealthInstitution.objects.all()
    serializer = HealthInstitutionSerializer(health_institutions, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def health_institution_detail(request, id):
    try:
        health_institution = HealthInstitution.objects.get(id=id)
    except HealthInstitution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = HealthInstitutionSerializer(health_institution)
    return Response(serializer.data)
@api_view(['POST'])
def health_institution_create(request):
    serializer = SingleHealthInstitutionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['PUT'])
def health_institution_update(request, id):
    try:
        health_institution = HealthInstitution.objects.get(id=id)
    except HealthInstitution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SingleHealthInstitutionSerializer(health_institution, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['DELETE'])
def health_institution_delete(request, id):
    try:
        health_institution = HealthInstitution.objects.get(id=id)
    except HealthInstitution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    health_institution.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def health_institution_search(request, name):
    health_institutions = HealthInstitution.objects.filter(name__icontains=name)
    serializer = HealthInstitutionSerializer(health_institutions, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def health_institution_search_by_location(request, location):
    health_institutions = HealthInstitution.objects.filter(location__icontains=location)
    serializer = HealthInstitutionSerializer(health_institutions, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def health_institution_search_by_speciality(request, speciality):
    health_institutions = HealthInstitution.objects.filter(speciality__icontains=speciality)
    serializer = HealthInstitutionSerializer(health_institutions, many=True)
    return Response(serializer.data)


