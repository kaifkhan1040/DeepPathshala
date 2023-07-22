from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('course_single/<int:id>',course_single,name='course_single'),
    path('play/<int:id>',play,name='play'),
    path('enroll/<int:id>',enroll_user,name='enrol_user'),



]
