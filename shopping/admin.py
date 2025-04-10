from django.contrib import admin
from .models import Class, Teacher, Student, ClassTime
# Register your models here.
@admin.register(Class)
class AdminClass(admin.ModelAdmin):
    list_display = ['class_name','class_day','class_time','class_date','teacher']

@admin.register(ClassTime)
class AdminClassTime(admin.ModelAdmin):
    list_display = ['time_start']

@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ['name','email','phone']

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['name']
