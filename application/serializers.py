import serpy
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        depth=2
        model = Application
        fields = '__all__'


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = []

    def create(self, validated_data):
        # Create a new application
        application = get_user_model().objects.create(**validated_data)
        application.save()

        return application

