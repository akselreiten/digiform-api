from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import UniversityReview
from .serializers import UniversityReviewSerializer, UniversityReviewCreateSerializer


# Create your views here.
class UniversityReviewListCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    #get review by university
    def get(self, request):
        if request.GET.get("uni") != "": #if filter is active
            university_reviews = UniversityReview.objects.filter(university__id=request.GET.get("uni")) #filter by university
            data = UniversityReviewSerializer(university_reviews, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_200_OK) #if filter not active, return empty list

    #create review
    def post(self, request):
        serializer = UniversityReviewCreateSerializer(data=request.data) #serialize
        serializer.is_valid(raise_exception=True) #error handling
        university_review = serializer.save(user=request.user) #save by user
        data = UniversityReviewSerializer(university_review).data #retrieve data
        return Response(data, status=status.HTTP_201_CREATED) #201 ok