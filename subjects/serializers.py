import serpy
from rest_framework import serializers

from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Subject
        fields = '__all__'


class SubjectCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'
