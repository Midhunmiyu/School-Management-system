from django.contrib import admin

from home.models import Login, Teacher, Student

# Register your models here.
admin.site.register(Login)
admin.site.register(Teacher)
admin.site.register(Student)