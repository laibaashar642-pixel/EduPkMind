from django.urls import path,include
from courses.views import add_course,add_lesson,course_list,enroll_course
urlpatterns = [
   
    path('add/',add_course,name='add_course'),
    path('lesson/add/<int:course_id>/', add_lesson, name='add_lesson'),
    path('list/', course_list, name='course_list'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
   
]
