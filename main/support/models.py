from django.db import models
from users.models import CustomUser

class Support(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='support_tickets')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=[('open', 'Open'), ('closed', 'Closed')], default='open')
    created_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.subject