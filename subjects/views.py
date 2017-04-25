from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subject
from .serializers import SubjectSerializer, SubjectCreateSerializer


# Create your views here.
class SubjectListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, )
    queryset = Subject.objects.filter() #find all objects
    serializer_class = SubjectSerializer

    #-- example filters --
    #queryset = Subject.objects.filter(title__contains="obj")
    #queryset = queryset.filter(university__id=1)

    '''
    def get(self,request):
        queryset = Subject.objects.filter(title__contains="obj")
        queryset = queryset.filter(university__id=1)
        serializer = SubjectSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''

    def post(self, request):
        serializer = SubjectCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.save()
        data = SubjectSerializer(subject).data
        return Response(data, status=status.HTTP_201_CREATED)

class SubjectCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,pk):
        queryset = Subject.objects.filter(id=pk)
        data = SubjectSerializer(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)