from .models import Course, Faculty, Teacher
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, get_object_or_404

from .models import Course, Faculty, Teacher


def index(request):
    num_course = Course.objects.count()
    num_teacher = Teacher.objects.count()
    num_faculty = Faculty.objects.count() 

    return render(
        request,
        'index.html',
        context={
            'num_course': num_course,
            'num_teacher': num_teacher,
            'num_faculty': num_faculty  
        }
    )


def course_list(request):
    return render(
        request,
        'course_list.html',
        context={
            'course_list': Course.objects.all()
        }
    )


def teacher_list(request):
    return render(
        request,
        'teacher_list.html',
        context={
            'teacher_list': Teacher.objects.all()
        }
    )


def course_detail(request, id):
    course = get_object_or_404(Course, pk=id)
    return render(request, 'course_detail.html', {'course': course})


def teacher_detail(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})

