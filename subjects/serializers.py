import serpy
from rest_framework import serializers

from .models import Subject


#serialzier for getting subjects
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2 #for filtering purposes
        model = Subject
        fields = '__all__'


#serializer for creating subjects
class SubjectCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'
