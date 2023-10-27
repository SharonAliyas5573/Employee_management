
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    manager = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        null=True,
        related_name='managed_department',
        default=-1  
    )

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    date_of_joining = models.DateField()
    years_of_experience = models.IntegerField()
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        default=-1  
    )
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.name