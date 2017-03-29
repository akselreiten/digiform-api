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
from django.db.models import Q


# Create your views here.

class MessageListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        inbox = Message.objects.filter(Q(receiver=request.user) | Q(sender=request.user)).order_by('-time_stamp')

        serializer = MessageSerializer(inbox, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
