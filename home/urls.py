from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from home import views, adminviews

urlpatterns = [

    path('', views.signin, name='signin'),
    path('registrationbase', views.registrationbase, name='registrationbase'),
    path('teachersignup', views.teachersignup, name='teachersignup'),
    path('studentsignup', views.studentsignup, name='studentsignup'),



# admin urls

    path('admindashboard', adminviews.admindashboard, name='admindashboard'),


# teacher urls





# student urls



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
