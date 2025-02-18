from django import template
from courses.models import Course, Category

register = template.Library()

@register.inclusion_tag('courses/latest_courses.html')
def show_latest_courses(count=5):
    latest_courses = Course.objects.order_by('-created_date')[:count]
    return {'latest_courses': latest_courses}

@register.inclusion_tag('courses/categories.html')
def category_tree():
    categories = Category.objects.filter(parent_category__isnull=True)  # فقط دسته‌های اصلی
    return {'categories': categories}