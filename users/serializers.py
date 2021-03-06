import serpy
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serpy.Serializer):

    #user id
    id = serpy.IntField()

    #username
    username = serpy.StrField()

    #user email
    email = serpy.StrField()

    #first name
    first_name = serpy.Field(required=False)

    #last name
    last_name = serpy.Field(required=False)

    #status
    is_active = serpy.BoolField()

    #to-string
    def __str__(self):
        return self.first_name + " " + self.last_name


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []

    def create(self, validated_data):
        #create the authenticated user
        user = get_user_model().objects.create(**validated_data)

        #set password
        user.set_password(validated_data['password'])
        user.save()

        return user

