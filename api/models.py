from django.db import models
from django.utils import timezone

# Create your models here.

class DetectionHistory(models.Model):
    image = models.ImageField(upload_to='detection_history/')
    processed_image = models.TextField()  # Store base64 encoded image
    detections = models.JSONField()  # Store detection results as JSON
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']  # Most recent first

    def __str__(self):
        return f"Detection from {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
