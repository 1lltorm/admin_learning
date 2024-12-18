from django.db import models
from django.urls import reverse


class Faculty(models.Model):
    name = models.CharField(max_length=200, help_text="Введите наименование факультета")

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Введите описание учебного курса")
    faculty = models.ManyToManyField(Faculty, help_text="Выберите факультет")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('firstapp:course_detail', args=[str(self.id)])

    def display_faculty(self):
        return ', '.join([faculty.name for faculty in self.faculty.all()[:3]])  # возвращает строку

    display_faculty.short_description = 'Faculty'


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('firstapp:teacher_detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
