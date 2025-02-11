from django.shortcuts import render
from courses.models import Course
from django.views.generic import DetailView


def index(req):
    carousel_courses = Course.objects.all()
    return render(req, 'index.html', context={'carousel_courses':carousel_courses})


class CourseDetailView(DetailView):
    model = Course
    template_name = ''