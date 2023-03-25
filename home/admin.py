from django.contrib import admin

from home.models import Login, Teacher, Student, Course, Subject, StudentFeedback, TeacherFeedback

# Register your models here.
admin.site.register(Login)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(StudentFeedback)
admin.site.register(TeacherFeedback)
