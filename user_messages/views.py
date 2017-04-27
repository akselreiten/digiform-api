from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from itertools import chain
from operator import attrgetter
from django.db.models import Q
from .models import Message
from .serializers import MessageSerializer, MessageCreateSerializer
from django.db.models import Q



# Create your views here.

class MessageListView(APIView):
    permission_classes = (IsAuthenticated,)

    #get all messages to or from user
    def get(self, request):
        inbox = Message.objects.filter(Q(receiver=request.user) | Q(sender=request.user)).order_by('-time_stamp') #sort messages by time stamp
        serializer = MessageSerializer(inbox, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    #create message to and from user.
    #a little bit unconventional, but works!
    def post(self, request):
        serializer = MessageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.save(sender=request.user, receiver = request.user)
        data = MessageSerializer(message).data
        return Response(data, status=status.HTTP_201_CREATED)



