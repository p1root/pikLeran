from courses.models import Course
from django.views.generic import DetailView


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'