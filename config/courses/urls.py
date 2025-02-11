from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('course/<int:id>', views.CourseDetailView.as_view(), name='course-detail')
]