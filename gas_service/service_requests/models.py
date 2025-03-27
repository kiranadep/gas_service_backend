from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('gas_leak', 'Gas Leak'),
        ('meter_issue', 'Meter Issue'),
        ('billing', 'Billing Problem'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)  
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request {self.id} - {self.request_type}"
