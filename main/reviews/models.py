from django.db import models
from users.models import CustomUser
from courses.models import Course

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"