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

    def get(self, request):
        university_reviews = UniversityReview.objects.filter(university__id=request.GET.get("uni"))
        data = UniversityReviewSerializer(university_reviews, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UniversityReviewCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        university_review = serializer.save(user=request.user)
        data = UniversityReviewSerializer(university_review).data
        return Response(data, status=status.HTTP_201_CREATED)