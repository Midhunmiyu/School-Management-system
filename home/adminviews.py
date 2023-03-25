from django.shortcuts import render, redirect

from home.forms import CourseForm, TeacherForm, LoginForm, SubjectForm
from home.models import Course, Teacher, Student, Subject, StudentFeedback, TeacherFeedback


def admindashboard(request):
    return render(request, 'admin1/Adminbase.html')


def add_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_course')
    return render(request, 'admin1/Addcourse.html', {'form': form})


def view_course(request):
    data = Course.objects.all()
    return render(request, 'admin1/Viewcourse.html', {'data': data})


def delete_course(request, id):
    data = Course.objects.get(id=id)
    data.delete()
    return redirect('view_course')


def view_teachers(request):
    data = Teacher.objects.all()
    return render(request, 'admin1/Viewteachers.html', {'data': data})


def delete_teacher(request, id):
    data = Teacher.objects.get(id=id)
    data.delete()
    return redirect('view_teacher')


def view_students(request):
    data = Student.objects.all()
    return render(request, 'admin1/Viewstudents.html', {'data': data})


def delete_student(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('view_students')


def add_students(request):
    return render(request, 'admin1/Addstudents.html')


def add_subject(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_subjects')

    return render(request, 'admin1/Addsubjects.html', {'form': form})


def view_subjects(request):
    data = Subject.objects.all()
    return render(request, 'admin1/viewsubjects.html', {'data': data})


def delete_subject(request, id):
    data = Subject.objects.get(id=id)
    data.delete()
    return redirect('view_subjects')


def student_feedbacks(request):
    data = StudentFeedback.objects.all()
    return render(request, 'admin1/Studentfeedbacks.html', {'data': data})


def reply_student_feedbacks(request, id):
    data = StudentFeedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('Reply', )
        data.Reply = r
        data.save()
        return redirect('student_feedbacks')
    return render(request, 'admin1/Replystudent.html', {'data': data})


def teacher_feedbacks(request):
    data = TeacherFeedback.objects.all()
    return render(request, 'admin1/Teacherfeedbacks.html', {'data': data})


def reply_teacher_feedbacks(request, id):
    data = TeacherFeedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('Reply', )
        data.Reply = r
        data.save()
        return redirect('teacher_feedbacks')
    return render(request, 'admin1/Replystudent.html', {'data': data})
