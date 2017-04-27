import serpy
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Application


#serializer for getting own applications
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2  #allows foreign key accessing
        model = Application
        fields = '__all__'

#serializer for creating new application
class ApplicationCreateSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField()

    class Meta:
        model = Application
        fields = '__all__'

#serializer for getting several applications
#used for subject filtering
class AllApplicationsSerializer(serializers.ModelSerializer):

    university_id = serpy.IntField()
    ntnu_subject_id = serpy.IntField()
    approval_id = str

    class Meta:
        depth = 2  #allows foreign key accessing
        model = Application
        fields = '__all__'