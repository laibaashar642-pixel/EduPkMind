
from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

from .models import Course
from .models import Lesson
from .models import Enrollment
def add_course(request):
    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        # database mein save karo
        Course.objects.create(
            title=title,
            description=description,
            teacher_id=request.session['user_id']
        )
        return redirect('teacher_dashboard')

    return render(request,"courses/course.html" )
def add_lesson(request, course_id):
       if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Lesson.objects.create(
            title=title,
            content=content,
            course_id=course_id
        )
        return redirect('teacher_dashboard')
       return render(request, "courses/add_lesson.html")
def course_list(request):
    courses=Course.objects.all()
    return render(request,"courses/list.html",{'courses':courses})
def enroll_course(request, course_id):
    Enrollment.objects.create(
        student_id=request.session['user_id'],
        course_id=course_id
    )
    return redirect('student_dashboard')
