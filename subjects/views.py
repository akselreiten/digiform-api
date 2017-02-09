from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Subject
from .serializers import SubjectSerializer


# Create your views here.
class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (AllowAny, )