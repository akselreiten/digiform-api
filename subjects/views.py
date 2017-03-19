from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import Subject
from .serializers import SubjectSerializer, SubjectCreateSerializer


# Create your views here.
class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        subjects = Subject.objects.filter(user=request.user)
        data = SubjectSerializer(subjects, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SubjectCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.save(user=request.user)
        data = SubjectSerializer(subject).data
        return Response(data, status=status.HTTP_201_CREATED)


class NtnuSubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.filter(university__title='NTNU')
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, )
