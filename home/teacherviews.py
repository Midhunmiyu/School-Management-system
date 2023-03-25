from django.shortcuts import render, redirect

from home.forms import TeacherFeedbackForm
from home.models import Teacher, Course, Subject, Student, TeacherFeedback


def teacherdashboard(request):
    return  render(request,'teacher/Teacherbase.html')


def teachers_list(request):
    data=Teacher.objects.all()
    return render(request,'Teacher/Teacherslist.html',{'data':data})


def teacher_view_course(request):
    data=Course.objects.all()
    return render(request,'Teacher/Viewcourses.html',{'data':data})


def teacher_view_subjects(request):
    data=Subject.objects.all()
    return render(request,'Teacher/Viewsubjects.html',{'data':data})


def teacher_view_students(request):
    data=Student.objects.all()
    return render(request,'Teacher/Viewstudents.html',{'data':data})


def teacher_add_feedback(request):
    form = TeacherFeedbackForm()
    u = request.user
    if request.method == "POST":
        form = TeacherFeedbackForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = u
            a.save()
            return redirect('teacher_view_feedback')
    return render(request,'Teacher/Addfeedbacks.html',{'form':form})


def teacher_view_feedback(request):
    data = TeacherFeedback.objects.all()
    return render(request,'Teacher/Viewfeedbacks.html',{'data':data})