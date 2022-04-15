from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'Department : {self.department} & Location : {self.location}'

class Role(models.Model):
    designation = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Designation : {self.designation}, Department : {self.department}'

class Employee(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(default=18)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Don`t want to disclose')
    )
    gender = models.CharField(null=False, max_length=5, choices=gender_choices)
    phone = models.CharField(max_length=20, default=0,null=False, unique=True)
    email = models.EmailField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Role, on_delete=models.CASCADE)
    date_join = models.DateField()
    salary = models.IntegerField(default=0,null=False)
    HRA_variables = models.IntegerField(default=0,null=False)
    incentives = models.IntegerField(default=0,null=False)
    address = models.TextField(max_length=1024, null=False,default='Hyderabad')

    def __str__(self):
        return f"Employee Name : {self.first_name} & Employee ID : {self.id}"

