from django.urls import path
from .views import course_list, course_detail

urlpatterns = [
    path('', course_list, name='course-list'),
    path('<int:id>/', course_detail, name='course-detail'),
]
