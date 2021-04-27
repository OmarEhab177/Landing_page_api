from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'name',
            'email',
            'created_date'
        )
        read_only_fields = (
            'date_created',
        )