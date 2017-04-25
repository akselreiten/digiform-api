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
    permission_classes = (IsAuthenticated,)

    def get(self,request):

        applications = Application.objects.filter()

        if request.GET.get("uni") != "":
            applications = applications.filter(replacing_subject__university__id = request.GET.get("uni"))
        if request.GET.get("subject") != "":
            applications = applications.filter(ntnu_subject__id = request.GET.get("subject"))
        if request.GET.get("approval") != "":
            applications = applications.filter(application_status = "Accepted")


        data = AllApplicationsSerializer(applications,many=True).data

        return Response(data, status=status.HTTP_200_OK)

class ApplicationListCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        applications = Application.objects.filter(user=request.user)
        data = ApplicationSerializer(applications, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ApplicationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.save(user=request.user)
        data = ApplicationSerializer(application).data
        return Response(data, status=status.HTTP_201_CREATED)
