from django.db import models
from  users.models import CustomUser
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته ی مادر')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'دسته بندی ها'
        verbose_name = 'دسته بندی'

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='موضوع')
    thumbnail = models.FileField(upload_to='course_thumbnails', max_length=100, verbose_name='عکس دوره')
    description = models.TextField(verbose_name='توضیحات')
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='courses_taught', verbose_name='مربی')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='دسته بندی')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')
    duration = models.DurationField(verbose_name='مدت')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='اخرین ویرایش')
    status = models.CharField(max_length=10, choices=[('published', 'منتشر شده'), ('draft', 'پیش نویس')], default='draft', verbose_name='وضعیت')
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('courses:detail' , args=[self.id])
    
    class Meta:
        verbose_name_plural = 'دوره ها'
        verbose_name = 'دوره'
    
class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos', verbose_name='دوره ی')
    title = models.CharField(max_length=200, verbose_name='نام')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    url = models.URLField(verbose_name='آدرس')
    duration = models.DurationField(verbose_name='مدت زمان')
    order = models.PositiveIntegerField(verbose_name='ترتیب')
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ آپلود')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'ویدئو'
        verbose_name = 'ویدئو ها'

class UserProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='progress', verbose_name='کاربر')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='progress', verbose_name='دوره')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='progress', verbose_name='ویدئو')
    completion_status = models.CharField(max_length=11, choices=[('watched', 'Watched'), ('not_watched', 'Not Watched')], default='not_watched', verbose_name='وضعیت')
    last_watched = models.DateTimeField(auto_now=True, verbose_name='آخرین تاریخ دیده شده')

    def __str__(self):
        return f"{self.user.username} - {self.video.title}"

    class Meta:
        verbose_name_plural = 'وضعیت کاربران'
        verbose_name = 'وضعیت کاربر'