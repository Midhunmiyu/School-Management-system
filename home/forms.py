from django import forms
from django.contrib.auth.forms import UserCreationForm

from home.models import Login, Teacher, Student, Course, Subject, StudentFeedback, TeacherFeedback


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ('user',)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ('user',)


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentFeedbackForm(forms.ModelForm):
    class Meta:
        model = StudentFeedback
        fields = '__all__'
        exclude = ('Reply','user',)


class TeacherFeedbackForm(forms.ModelForm):
    class Meta:
        model = TeacherFeedback
        fields = '__all__'
        exclude = ('Reply','user',)
