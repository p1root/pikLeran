from django.db import models
from users.models import CustomUser

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    notification_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('read', 'Read'), ('unread', 'Unread')], default='unread')

    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name_plural = 'اعلانات'
        verbose_name = 'اعلان'