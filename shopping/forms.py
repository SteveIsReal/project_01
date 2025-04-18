from django import forms
from .models import ClassTime, Class, Teacher, Student

class ClassTimeForm(forms.ModelForm):
    class Meta:
        model = ClassTime
        fields = ['time_start','time_end']
        
class ClassForm(forms.ModelForm):
    class Meta:
        model =  Class
        fields = ['class_name','class_day','class_time','class_date','teacher','students']
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name","phone","email"]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name"]
