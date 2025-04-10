from django.urls import path
from . import views
urlpatterns = [
        path("create_class/", views.create_class, name="create_class"),
        path("teacher_register/", views.teacher_register, name="teacher"),
        path("student_register/",views.student_register, name="student"),
        path("time_register/",views.time_register, name="time"),
        path("/", views.display_page, name="display")
        ]
