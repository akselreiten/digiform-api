from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Subject
from .serializers import SubjectSerializer, SubjectCreateSerializer


# Create your views here.
class SubjectListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, ) #authentication
    queryset = Subject.objects.filter() #find all objects
    serializer_class = SubjectSerializer #seralize


    def post(self, request):
        serializer = SubjectCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.save()
        data = SubjectSerializer(subject).data
        return Response(data, status=status.HTTP_201_CREATED) #201 created

class SubjectCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,pk):
        queryset = Subject.objects.filter(id=pk) #filter on the pk id
        data = SubjectSerializer(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK) #200 ok