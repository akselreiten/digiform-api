import serpy
from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        depth = 1
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField()
    receiver = serializers.ReadOnlyField()

    class Meta:
        model = Message
        fields = '__all__'


