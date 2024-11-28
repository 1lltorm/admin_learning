from django.contrib import admin
from django.urls import path
from firstapp import views  # Импортируем views из приложения firstapp

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь для админки
    path('', views.index, name='index'),  # Путь для главной страницы
    path('courses/', views.course_list, name='course_list'),  # Путь для списка курсов
    path('teachers/', views.teacher_list, name='teacher_list'),  # Путь для списка преподавателей
    path('course/<int:id>/', views.course_detail, name='course_detail'),  # Путь для подробностей курса
    path('teacher/<int:id>/', views.teacher_detail, name='teacher_detail'),  # Путь для подробностей преподавателя
    path('course_list_view/', views.CourseListView.as_view(), name='course_list_view'),  # Путь для представления на основе класса
]
