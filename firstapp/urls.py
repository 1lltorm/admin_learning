from django.urls import path

from . import views

app_name = 'firstapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('course/', views.course_list, name='course'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('teacher/<int:id>/', views.teacher_detail, name='teacher_detail'),
    path('teacher/', views.teacher_list, name='teacher_list')
]




urlpatterns = [
    path("", views.index, name="index"),
    path("course/", views.courseListView.as_view(), name="course"),
    path("course/<int:pk>/", views.courseDetailView.as_view(), name="course_detail"),
]