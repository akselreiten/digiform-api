import serpy
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Review


class UniversityReviewSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Review
        fields = '__all__'


class UniversityReviewCreateSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField()

    class Meta:
        model = Review
        fields = '__all__'
