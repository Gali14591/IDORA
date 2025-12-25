from rest_framework import serializers
from .models import Inbox
from sends.serializers import SendSerializer


class InboxSerializer(serializers.ModelSerializer):
    send = SendSerializer(read_only=True)
    
    class Meta:
        model = Inbox
        fields = ('id', 'send', 'is_read', 'read_at')
        read_only_fields = ('id', 'read_at')

