from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from home.forms import LoginForm, TeacherForm, StudentForm


# Create your views here

def registrationbase(request):
    return render(request, 'registrationbase.html')


def teachersignup(request):
    form1 = LoginForm()
    form2 = TeacherForm()
    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        form2 = TeacherForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_teacher = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()
        return redirect('signin')
    return render(request, 'teachersignup.html', {'form1': form1, 'form2': form2})


def studentsignup(request):
    form1 = LoginForm()
    form2 = StudentForm()
    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        form2 = StudentForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_student = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()
        return redirect('signin')
    return render(request, 'studentsignup.html', {'form1': form1, 'form2': form2})


def signin(request):
    if request.method == 'POST':
        username = request.method.POST.get('uname')
        password = request.method.POST.get('Pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request.user)
            if user.is_staff:
                return redirect('admindashboard')
            if user.is_teacher:
                pass
                # return redirect('Teacherdashboard')
            if user.is_student:
                pass
                # return redirect('Studentdashboard')

        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'signin.html')
