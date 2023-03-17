from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Name


class Student(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()

    def __str__(self):
        return self.Name
