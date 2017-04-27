from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import University
from .serializers import UniversitySerializer

from subjects.models import Subject
from subjects.serializers import SubjectSerializer



#get all universities
class UniversityListCreateView(generics.ListCreateAPIView):
    queryset = University.objects.all() #no filter
    serializer_class = UniversitySerializer #serialize
    permission_classes = (IsAuthenticated,) #check authentication


class UniversityListSubjectView(APIView):
    permission_classes = (IsAuthenticated,) #check authentication

    def get(self, request, pk):
        subjects = Subject.objects.filter(university_id=pk) #get specific university
        serializer = SubjectSerializer(subjects, many=True) #serialize
        return Response(serializer.data, status=status.HTTP_200_OK) #200 ok

class UniversitySearchListCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        unis = University.objects.filter() #filter in all universities

        if request.GET.get("title_contains") != "": #if filter is active
            unis = unis.filter(title__contains = request.GET.get("title_contains"))
        if request.GET.get("city") != "": #if filter is active
            unis = unis.filter(city = request.GET.get("city"))
        if request.GET.get("country") != "": #if filter is active
            unis = unis.filter(country = request.GET.get("country"))

        data = UniversitySerializer(unis, many=True).data

        return Response(data, status=status.HTTP_200_OK)#200 ok
