from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Send
from .serializers import SendSerializer
from accounts.models import User
from documents.models import Document


class SendViewSet(viewsets.ModelViewSet):
    serializer_class = SendSerializer
    
    def get_queryset(self):
        return Send.objects.filter(sender=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        recipient_phone = serializer.validated_data.pop('recipient_phone')
        document_id = serializer.validated_data.pop('document_id')
        
        try:
            recipient = User.objects.get(phone=recipient_phone)
            document = Document.objects.get(id=document_id, owner=request.user)
        except User.DoesNotExist:
            return Response({'error': 'Recipient not found'}, status=status.HTTP_404_NOT_FOUND)
        except Document.DoesNotExist:
            return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)
        
        send = serializer.save(sender=request.user, recipient=recipient, document=document)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

