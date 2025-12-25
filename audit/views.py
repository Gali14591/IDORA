from rest_framework import viewsets
from .models import AuditLog
from .serializers import AuditLogSerializer


class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuditLogSerializer
    
    def get_queryset(self):
        return AuditLog.objects.filter(user=self.request.user)

