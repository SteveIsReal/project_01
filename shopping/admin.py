from django.contrib import admin
from .models import Class, Teacher, Student
# Register your models here.
@admin.register(Class)
class AdminClass(admin.ModelAdmin):
    list_display = ['class_name','class_day','class_time','teacher']

@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ['name','email','phone']

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['name']
