from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.CourseDetailView.as_view(), name='course-detail')
]