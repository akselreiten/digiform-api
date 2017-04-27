from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Application
from .serializers import ApplicationSerializer, ApplicationCreateSerializer, AllApplicationsSerializer




# Create your views here.


class AllApplicationsListCreateView(APIView):
    permission_classes = (IsAuthenticated,) #user must be logged in

    def get(self,request):

        applications = Application.objects.filter() #filter in all objects

        if request.GET.get("uni") != "": #if filter has a value
            applications = applications.filter(replacing_subject__university__id = request.GET.get("uni"))
        if request.GET.get("subject") != "": #if filter has a value
            applications = applications.filter(ntnu_subject__id = request.GET.get("subject"))
        if request.GET.get("approval") != "": #if filter has a value
            applications = applications.filter(application_status = "Accepted")

        #serialize data
        data = AllApplicationsSerializer(applications,many=True).data

        #expected 200 ok
        return Response(data, status=status.HTTP_200_OK)

class ApplicationListCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request): #get all applications submitted by the logged in user
        applications = Application.objects.filter(user=request.user) #filter
        data = ApplicationSerializer(applications, many=True).data #serialize
        return Response(data, status=status.HTTP_200_OK) #200 ok

    def post(self, request): #create new application
        serializer = ApplicationCreateSerializer(data=request.data) #serialize
        serializer.is_valid(raise_exception=True) #error handling
        application = serializer.save(user=request.user) #save serialized object
        data = ApplicationSerializer(application).data #get data
        return Response(data, status=status.HTTP_201_CREATED) #return response 201
