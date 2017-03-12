
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from .models import Application
from .serializers import ApplicationSerializer, ApplicationCreateSerializer


# Create your views here.
class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticated, )


class ApplicationListCreate(APIView):
    """
    Create application view
    """
    permission_classes = [permissions.AllowAny]


    def post(self, request):
        serializer = ApplicationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.save()
        data = ApplicationSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
