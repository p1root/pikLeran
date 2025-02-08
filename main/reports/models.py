from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('sales', 'Sales Report'),
        ('users', 'Users Report'),
        ('courses', 'Courses Report'),
        ('payments', 'Payments Report'),
        # می‌توانید انواع دیگر گزارش‌ها را اضافه کنید
    ]

    report_type = models.CharField(max_length=50, choices=REPORT_TYPE_CHOICES)
    generated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reports_generated')
    generated_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=True, null=True)  # تاریخ شروع بازه گزارش
    end_date = models.DateTimeField(blank=True, null=True)    # تاریخ پایان بازه گزارش
    data = models.JSONField(default=dict)  # ذخیره داده‌های گزارش به صورت JSON
    file = models.FileField(upload_to='reports/', blank=True, null=True)  # اگر گزارش به صورت فایل ذخیره شود

    def __str__(self):
        return f"{self.get_report_type_display()} - {self.generated_date.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        ordering = ['-generated_date']
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'