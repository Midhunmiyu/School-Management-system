from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from home import views, adminviews, teacherviews, studentviews

urlpatterns = [

    path('', views.signin, name='signin'),
    path('registrationbase', views.registrationbase, name='registrationbase'),
    path('teachersignup', views.teachersignup, name='teachersignup'),
    path('studentsignup', views.studentsignup, name='studentsignup'),

    # admin urls

    path('admindashboard', adminviews.admindashboard, name='admindashboard'),
    path('admindashboard/course/add', adminviews.add_course, name='add_course'),
    path('admindashboard/course/view', adminviews.view_course, name='view_course'),
    path('admindashboard/course/delete/<int:id>/', adminviews.delete_course, name='delete_course'),
    path('admindashboard/teachers/view', adminviews.view_teachers, name='view_teachers'),
    path('admindashboard/teachers/delete/<int:id>/', adminviews.delete_teacher, name='delete_teacher'),
    path('admindashboard/students/view', adminviews.view_students, name='view_students'),
    path('admindashboard/students/delete/<int:id>/', adminviews.delete_student, name='delete_student'),
    path('admindashboard/students/Add', adminviews.add_students, name='add_students'),
    path('admindashboard/subject/Add', adminviews.add_subject, name='add_subject'),
    path('admindashboard/subject/View', adminviews.view_subjects, name='view_subjects'),
    path('admindashboard/subjects/delete/<int:id>/', adminviews.delete_subject, name='delete_subject'),
    path('admindashboard/Studentfeedbacks', adminviews.student_feedbacks, name='student_feedbacks'),
    path('admindashboard/Studentfeedbacks/reply/<int:id>/', adminviews.reply_student_feedbacks, name='reply_student_feedbacks'),
    path('admindashboard/Teacherfeedbacks', adminviews.teacher_feedbacks, name='teacher_feedbacks'),
    path('admindashboard/Teacherfeedbacks/reply/<int:id>/', adminviews.reply_teacher_feedbacks, name='reply_teacher_feedbacks'),

    # teacher urls
    path('teacherdashboard', teacherviews.teacherdashboard, name='teacherdashboard'),
    path('teacherdashboard/teachers', teacherviews.teachers_list, name='teachers_list'),
    path('teacherdashboard/courses', teacherviews.teacher_view_course, name='teacher_view_course'),
    path('teacherdashboard/Subjects', teacherviews.teacher_view_subjects, name='teacher_view_subjects'),
    path('teacherdashboard/Studentslist', teacherviews.teacher_view_students, name='teacher_view_students'),
    path('teacherdashboard/feedback/Add', teacherviews.teacher_add_feedback, name='teacher_add_feedback'),
    path('teacherdashboard/feedback/view', teacherviews.teacher_view_feedback, name='teacher_view_feedback'),

    # student urls
    path('studentdashboard', studentviews.studentdashboard, name='studentdashboard'),
    path('studentdashboard/courses', studentviews.stud_view_course, name='stud_view_course'),
    path('studentdashboard/Teachers', studentviews.stud_view_teachers, name='stud_view_teachers'),
    path('studentdashboard/Subjects', studentviews.stud_view_subjects, name='stud_view_subjects'),
    path('studentdashboard/Feedback/add', studentviews.stud_add_feedback, name='stud_add_feedback'),
    path('studentdashboard/Feedback/view', studentviews.stud_view_feedback, name='stud_view_feedback'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
