from django.contrib import admin
from .models import Teacher, Faculty, Course

admin.site.register(Faculty)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'display_faculty')


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
