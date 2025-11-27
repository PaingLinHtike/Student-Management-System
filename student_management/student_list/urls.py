from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("create/", views.create_student, name="create_student"),
    path("edit/<str:id>/", views.edit_student, name="edit_student"),
    path("delete/<str:id>/", views.delete_student, name="delete_student"),
]
