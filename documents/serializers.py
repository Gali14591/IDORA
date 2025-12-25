from rest_framework import serializers
from .models import Document
from accounts.serializers import UserSerializer


class DocumentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    
    class Meta:
        model = Document
        fields = ('id', 'title', 'description', 'file', 'owner', 'created_at', 'updated_at')
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')

