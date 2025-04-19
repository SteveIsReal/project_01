from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from .models import TimeSlot, Course, Room


class RoomAdminForm(forms.ModelForm):
    def clean(self):
        data = super().clean()
        if Room.objects.filter(room_name=data["room_name"]).exists():
            raise ValidationError("Duplicate room name")
        else:
            return data


@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display = ['room_name']
    form = RoomAdminForm


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ['name']

@admin.register(TimeSlot)
class AdminTimeSlot(admin.ModelAdmin):
    list_display = ['course','room']
