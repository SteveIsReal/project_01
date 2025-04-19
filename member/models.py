from django.db import models
from classroom.models import TimeSlot 


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

class Enrollment(models.Model):
   timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
   teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
   student = models.ManyToManyField(Student)
   
   def __str__(self):
       return 'Class' 
