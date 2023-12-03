from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Professional
from .serializers import ProfessionalsSerializer, ProfessionalSingleSerializer
from rest_framework import status

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

# @api_view(['GET'])
# def professional_association_list(request):
#     professionals = Professional.objects.all()
#     serializer = ProfessionalsSerializer(professionals, many=True)
#     return Response(serializer.data)
# @api_view(['GET'])
# def professional_association_detail(request, id):
#     try:
#         professional = Professional.objects.get(id=id)
#     except Professional.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = ProfessionalSerializer(professional)
#     return Response(serializer.data)
# @api_view(['POST'])
# def professional_association_create(request):
#     serializer = ProfessionalsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)
# @api_view(['PUT'])
# def professional_association_update(request, id):
#     try:
#         professional = Professional.objects.get(id=id)
#     except Professional.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = ProfessionalsSerializer(professional, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)
# @api_view(['DELETE'])
# def professional_association_delete(request, id):
#     try:
#         professional = Professional.objects.get(id=id)
#     except Professional.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     professional.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)