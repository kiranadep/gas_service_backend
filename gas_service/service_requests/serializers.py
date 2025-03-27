from rest_framework import serializers
from .models import ServiceRequest

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['user', 'request_type', 'description', 'attachment', 'status', 'created_at']
