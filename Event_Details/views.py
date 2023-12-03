from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EventDetails
from rest_framework import status
from .serializers import EventSerializer
from .serializers import EventDetailsSerializer, singleEventSerializer
@api_view(['GET'])
def event_details_list(request):
    event_details = EventDetails.objects.all()
    serializer = EventSerializer(event_details, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def event_details_detail(request, id):
    try:
        event_details = EventDetails.objects.get(id=id)
    except EventDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EventSerializer(event_details)
    return Response(serializer.data)
@api_view(['POST'])
def event_details_create(request):
    serializer = singleEventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['PUT'])
def event_details_update(request, id):
    try:
        event_details = EventDetails.objects.get(id=id)
    except EventDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = singleEventSerializer(event_details, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['DELETE'])
def event_details_delete(request, id):
    try:
        event_details = EventDetails.objects.get(id=id)
    except EventDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    event_details.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



