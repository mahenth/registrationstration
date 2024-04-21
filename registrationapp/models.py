from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100, help_text="Student's first name.")
    last_name = models.CharField(max_length=100, help_text="Student's last name.")
    email = models.EmailField(help_text="Student's email address.")
    mobile_number = models.CharField(max_length=15, help_text="Student's mobile number.")
    address = models.CharField(max_length=200, help_text="Student's address.")
    date_of_birth = models.DateField(help_text="Student's date of birth.")
    nationality = models.CharField(max_length=100, help_text="Student's nationality.")
    year = models.IntegerField(choices=[(i, i) for i in range(1, 5)], help_text="Student's academic year.")
    department = models.CharField(max_length=100, help_text="Student's department.")
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices, help_text="Student's gender")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
