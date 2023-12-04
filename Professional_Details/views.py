from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Professional
from Health_Institutions.models import HealthInstitution
from .serializers import ProfessionalsSerializer, ProfessionalSingleSerializer, UserSerializer
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['GET'])
def professional_list(request):
    professionals = Professional.objects.all()
    serializer = ProfessionalsSerializer(professionals, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def professional_detail(request, id):
    try:
        professional = Professional.objects.get(id=id)
    except Professional.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProfessionalsSerializer(professional)
    return Response(serializer.data)
@api_view(['POST'])
def professional_create(request):
    serializer = ProfessionalSingleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['PUT'])
def professional_update(request, id):
    try:
        professional = Professional.objects.get(id=id)
    except Professional.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProfessionalSingleSerializer(professional, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['DELETE'])
def professional_delete(request, id):
    try:
        professional = Professional.objects.get(id=id)
    except Professional.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    professional.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def professional_search(request, name):
    professionals = Professional.objects.filter(name__icontains=name)
    serializer = ProfessionalsSerializer(professionals, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def professional_search_by_hospital(request, hospital):
    health_institutions = HealthInstitution.objects.filter(name__icontains=hospital)
    if not health_institutions.exists():
        return Response({"error": f"No health institution found with the name '{hospital}'"}, status=404)
    hospital_instance = health_institutions.first()
    professionals = Professional.objects.filter(hospital=hospital_instance)
    serializer = ProfessionalsSerializer(professionals, many=True)
    return Response(serializer.data)
   
@api_view(['GET'])
def professional_search_by_profession(request, profession):
    professionals = Professional.objects.filter(profession__icontains=profession)
    serializer = ProfessionalsSerializer(professionals, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def professional_search_by_speciality(request, speciality):
    professionals = Professional.objects.filter(speciality__icontains=speciality)
    serializer = ProfessionalsSerializer(professionals, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_user(request, id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user)
    return Response(serializer.data)
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def create_user(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['PUT'])
def update_user(request):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['DELETE'])
def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
