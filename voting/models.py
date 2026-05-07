from django.db import models
from employees.models import Employee
from restaurants.models import Menu


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="votes")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="votes")
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("employee", "date")

    def __str__(self):
        return f"{self.employee} voted for {self.menu} on {self.date}"