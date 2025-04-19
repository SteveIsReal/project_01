from django.shortcuts import render, redirect
from .forms import ClassTimeForm, ClassForm, StudentForm, TeacherForm
# Create your views here.
def time_register(request):
    if request.method == "POST":
        form = ClassTimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ClassTimeForm()

    return render(request, "time_register/time_register.html", {'form':form})

def teacher_register(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TeacherForm()

    return render(request, "teacher_register/teacher_register.html", {'form':form})

def student_register(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = StudentForm()
    return render(request, "student_register/student_register.html", {'form':form})

def create_class(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ClassForm()
    return render(request, "create_class/create_class.html", {'form':form})

def display_page(request):

    return render(request, "display_page.html")

