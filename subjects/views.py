from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Subject
from .serializers import SubjectSerializer


# Create your views here.
class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, )


class NtnuSubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.filter(university__title='NTNU')
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, )
