from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MessageSerializer
from .models import Message
from api import serializers
# Create your views here.

@api_view(['GET'])
def messageList(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def messageDetail(request, pk):
    message = Message.objects.get(id=pk)
    serializer = MessageSerializer(message, many=False) 
    return Response(serializer.data)

@api_view(['POST'])
def messageCreate(request):
    serializer = MessageSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def messageUpdate(request, pk):
    message = Message.objects.get(id=pk)
    serializer = MessageSerializer(instance=message, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def messageDelete(request, pk):
    message = Message.objects.get(id=pk)
    message.delete()

    return Response("Deleted Successfully")