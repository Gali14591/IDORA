from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from .models import Inbox
from .serializers import InboxSerializer
from sends.models import Send


class InboxViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InboxSerializer
    
    def get_queryset(self):
        # Get all sends where the current user is the recipient
        sends = Send.objects.filter(recipient=self.request.user)
        # Create inbox items for sends that don't have one yet
        for send in sends:
            Inbox.objects.get_or_create(send=send)
        return Inbox.objects.filter(send__recipient=self.request.user)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.is_read:
            instance.is_read = True
            instance.read_at = timezone.now()
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

