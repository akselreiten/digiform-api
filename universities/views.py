from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import University
from .serializers import UniversitySerializer

from subjects.models import Subject
from subjects.serializers import SubjectSerializer


# Create your views here.
class UniversityListCreateView(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (IsAuthenticated,)


class UniversityListSubjectView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        subjects = Subject.objects.filter(university_id=pk)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
