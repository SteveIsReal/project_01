from django.db import models
from django import utils

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ClassTime(models.Model):
    time_start = models.TimeField(default=utils.timezone.now())
    time_end = models.TimeField(default=utils.timezone.now())

    def __str__(self):
        return f'{self.time_start} - {self.time_end}'

class Class(models.Model):
    weekday = [
            ('MONDAY','Monday'),
            ('TUESDAY','Tuesday'),
            ('WEDNESDAY','Wednesday'),
            ('THRUSDAY','Thrusday'),
            ('FRIDAY','Friday'),
            ('SATURDAY','Saturday'),
            ('SUNDAY','Sunday')
            ]
    class_name = models.CharField(max_length=50)
    class_day = models.CharField(max_length=20, choices=weekday)
    class_time = models.ForeignKey(ClassTime, on_delete=models.CASCADE)
    class_date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.class_name




