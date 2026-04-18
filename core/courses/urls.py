from django.urls import path
from . import views
urlpatterns=[
    path('',views.add_course,name='add_course'),
    path('lesson/add/<int:course_id>/', views.add_lesson, name='add_lesson'),
    path('list/', views.course_list, name='course_list'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    ]
