from django.contrib import admin
from .models import TimeSlot, Course, Room

@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display = ['room_name']

@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ['name']

@admin.register(TimeSlot)
class AdminTimeSlot(admin.ModelAdmin):
    list_display = ['course','room']
