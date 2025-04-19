from django.db import models
from django import utils


class Room(models.Model):
    room_name = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name


class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    weekday = [
            ('MONDAY','Monday'),
            ('TUESDAY','Tuesday'),
            ('WEDNESDAY','Wednesday'),
            ('THRUSDAY','Thrusday'),
            ('FRIDAY','Friday'),
            ('SATURDAY','Saturday'),
            ('SUNDAY','Sunday')
            ]
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    class_day = models.CharField(max_length=20, choices=weekday)
    time_start = models.TimeField(default=utils.timezone.now())
    time_end = models.TimeField(default=utils.timezone.now())

    def __str__(self):
        return f'{self.time_start} - {self.time_end}'



