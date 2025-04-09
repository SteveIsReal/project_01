from django.db import models

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
    times = [
            ('10.00-12.00','10.00-12.00'),
            ('13.00-15.00','13.00-15.00'),
            ('16.00-18.00','16.00-18.00'),
            ('17.00-19.00','17.00-19.00')
            ]
    class_name = models.CharField(max_length=50)
    class_day = models.CharField(max_length=20, choices=weekday)
    class_time = models.CharField(max_length=11, choices=times)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.class_name



