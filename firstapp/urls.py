from django.contrib import admin
from django.urls import path
from firstapp import views  # Импортируем views из приложения firstapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('courses/', views.course_list, name='course_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('teacher/<int:id>/', views.teacher_detail, name='teacher_detail'),
    path('course_list_view/', views.CourseListView.as_view(), name='course_list_view'),
]
