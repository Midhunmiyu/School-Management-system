from django.shortcuts import render, redirect

from home.forms import StudentFeedbackForm
from home.models import Course, Teacher, Subject, Student, StudentFeedback


def studentdashboard(request):
    return render(request, 'Students/Studentbase.html')


def stud_view_course(request):
    data = Course.objects.all()
    return render(request, 'Students/Viewcourse.html', {'data': data})


def stud_view_teachers(request):
    data = Teacher.objects.all()
    return render(request, 'Students/Viewteachers.html', {'data': data})


def stud_view_subjects(request):
    stud = Student.objects.get(user=request.user)
    data = Subject.objects.filter(course_name=stud.Course)
    return render(request, 'Students/Viewsubjects.html', {'data': data})


def stud_add_feedback(request):
    form = StudentFeedbackForm()
    u = request.user
    if request.method == "POST":
        form = StudentFeedbackForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = u
            a.save()
            return redirect('stud_view_feedback')
    return render(request, 'Students/Addfeedback.html', {'form': form})


def stud_view_feedback(request):
    data = StudentFeedback.objects.all()
    return render(request, 'Students/Viewfeedback.html', {'data': data})
