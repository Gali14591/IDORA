from django.db import models
from sends.models import Send


class Inbox(models.Model):
    send = models.OneToOneField(Send, on_delete=models.CASCADE, related_name='inbox_item')
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-send__sent_at']
    
    def __str__(self):
        return f"Inbox: {self.send.document.title}"

