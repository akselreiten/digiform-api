from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from itertools import chain
from operator import attrgetter
from django.db.models import Q
from .models import Message
from .serializers import MessageSerializer

# Create your views here.

class MessageListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        received_messages = Message.objects.filter(receiver=request.user)
        sent_messages = Message.objects.filter(sender=request.user)

        inbox = sorted(chain(received_messages,sent_messages),
                key=attrgetter('id'))

        serializer = MessageSerializer(inbox, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)