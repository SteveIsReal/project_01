from django.contrib import admin
from .models import Teacher, Student, Enrollment

@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ['name','phone','email']

    
@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Enrollment)
class AdminEnrollment(admin.ModelAdmin):
    list_display = ['timeslot','teacher']
