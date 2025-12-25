from rest_framework import serializers
from .models import Send
from accounts.serializers import UserSerializer
from documents.serializers import DocumentSerializer


class SendSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)
    document = DocumentSerializer(read_only=True)
    recipient_phone = serializers.CharField(write_only=True, required=True)
    document_id = serializers.IntegerField(write_only=True, required=True)
    
    class Meta:
        model = Send
        fields = ('id', 'sender', 'recipient', 'document', 'message', 'sent_at', 'read_at', 
                  'recipient_phone', 'document_id')
        read_only_fields = ('id', 'sender', 'sent_at', 'read_at')

