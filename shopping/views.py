from django.shortcuts import render

# Create your views here.
def time_register(request):
    return render(request, "time_register/time_register.html")

def teacher_register(request):
    return render(request, "teacher_register/teacher_register.html")

def student_register(request):
    return render(request, "student_register/student_register.html")

def create_class(request):
    return render(request, "create_class/create_class.html")

def display_page(request):
    return render(request, "display_page.html")

