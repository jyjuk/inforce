from django.urls import path
from . import views

urlpatterns = [
    path("", views.EmployeeCreateView.as_view(), name="employee-create"),
]