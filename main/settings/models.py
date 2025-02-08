from django.db import models

class SiteSettings(models.Model):
    setting_name = models.CharField(max_length=100, unique=True)
    setting_value = models.TextField()

    def __str__(self):
        return self.setting_name