import serpy
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UniversityReview


class UniversityReviewSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = UniversityReview
        fields = '__all__'


class UniversityReviewCreateSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField()

    class Meta:
        model = UniversityReview
        fields = '__all__'
