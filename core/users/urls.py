
from django.urls import path,include
from .views import index, signup, login, teacher_dashboard, student_dashboard
from .import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('teacher_dashboard/',views.teacher_dashboard,name='teacher_dashboard'),
    path('student_dashboard/',views.student_dashboard,name='student_dashboard'),
]