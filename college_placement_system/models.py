from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]

class User(AbstractUser):
    ROLE_CHOICES = [
        ('select role', 'Select Role'),
        ('admin', 'Admin'),
        ('hod', 'HOD'),
        ('student', 'Student'),
        ('company', 'Company')
    ]

    role = models.CharField(choices=ROLE_CHOICES,max_length=50)

class Student(models.Model):
   user = models.ForeignKey('User', on_delete=models.CASCADE)
   name = models.CharField(max_length=100)
   address = models.CharField(max_length=300)
   gender = models.CharField(choices=GENDER_CHOICES,max_length=5)
   email = models.EmailField()
   date_of_birth = models.DateField()
   phone = models.IntegerField()
   image = models.ImageField(default=False)
   branch = models.CharField(max_length=300)
   password = models.CharField(max_length=20)

class HOD(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=5)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=20)

class Company(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    website = models.URLField()
    email = models.EmailField()

class Job(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=300)
    twelfth_percentage = models.IntegerField()
    gpa = models.IntegerField()
    salary = models.CharField(max_length=10)

class JobApplication(models.Model):
    designation = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    experience = models.CharField(max_length=100)
    twelfth_percentage = models.IntegerField()
    gpa = models.IntegerField()
    no_of_seats = models.IntegerField()
    salary = models.CharField(max_length=10)
