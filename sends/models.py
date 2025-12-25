from django.db import models
from accounts.models import User
from documents.models import Document


class Send(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_documents')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_documents')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='sends')
    message = models.TextField(blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-sent_at']
    
    def __str__(self):
        return f"{self.sender.phone} -> {self.recipient.phone}: {self.document.title}"

