from django.shortcuts import render
from courses.models import Course

def index(req):
    carousel_courses = Course.objects.all()
    return render(req, 'index.html', context={'carousel_courses':carousel_courses})

