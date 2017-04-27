import serpy
from rest_framework import serializers

from .models import University


#university serializer
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
