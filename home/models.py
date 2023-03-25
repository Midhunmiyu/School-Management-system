import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_desc = models.TextField(max_length=200)

    def __str__(self):
        return self.course_name


class Teacher(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    Course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    Email = models.EmailField()
    Image = models.ImageField(upload_to='images/teachers')

    def __str__(self):
        return self.Name


class Student(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    Course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    Email = models.EmailField()
    Image = models.ImageField(upload_to='images/students')

    def __str__(self):
        return self.Name


class Subject(models.Model):
    course_name = models.ForeignKey(Course, models.DO_NOTHING)
    Subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Subject_name


class StudentFeedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    Feedback = models.CharField(max_length=200)
    Date = models.DateField(auto_now=True)
    Reply = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user

class TeacherFeedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    Feedback = models.CharField(max_length=200)
    Date = models.DateField(auto_now=True)
    Reply = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user
