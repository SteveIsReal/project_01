from django.shortcuts import render, redirect
from .forms import ClassTimeForm
# Create your views here.
def time_register(request):
    if request.method == "POST":
        form = ClassTimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_page')
    else:
        form = ClassTimeForm()

    return render(request, "time_register/time_register.html", {'form':form})

def teacher_register(request):
    return render(request, "teacher_register/teacher_register.html")

def student_register(request):
    return render(request, "student_register/student_register.html")

def create_class(request):
    return render(request, "create_class/create_class.html")

def display_page(request):
    return render(request, "display_page.html")

