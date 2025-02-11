from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>', views.CourseDetailView.as_view(), name='detail')
]