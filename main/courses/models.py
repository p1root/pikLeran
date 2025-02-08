from django.db import models
from  users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='courses_taught')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=[('published', 'Published'), ('draft', 'Draft')], default='draft')

    def __str__(self):
        return self.title
    
class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    duration = models.DurationField()
    order = models.PositiveIntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class UserProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='progress')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='progress')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='progress')
    completion_status = models.CharField(max_length=11, choices=[('watched', 'Watched'), ('not_watched', 'Not Watched')], default='not_watched')
    last_watched = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.video.title}"