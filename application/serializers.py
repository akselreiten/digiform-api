import serpy
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Application
        fields = '__all__'


class ApplicationCreateSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField()

    class Meta:
        model = Application
        fields = '__all__'

class AllApplicationsSerializer(serializers.ModelSerializer):

    university_id = serpy.IntField()
    ntnu_subject_id = serpy.IntField()
    approval_id = str

    class Meta:
        depth = 2
        model = Application
        fields = '__all__'