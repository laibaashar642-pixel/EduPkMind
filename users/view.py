

from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse

from courses.models import Enrollment
from courses.models import Courses
from users.models import User
def index(request):
     return render(request,'base.html')
def signup(request):
     if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        # Database mein save karo
        user = User.objects.create(
            username=username,
            email=email,
            password=password,
            role=role
        )
        return redirect('login')
     return render(request,'users/signup.html')
def login(request):
       if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Database mein dhundho
        user = User.objects.filter(
            username=username,
            password=password
        ).first()
        
        if user:
            # Session mein save karo
            request.session['user_id'] = user.id
            request.session['user_role'] = user.role
            
            # Role check karo
            if user.role == 'teacher':
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            return render(request, 'users/login.html', 
                        {'error': 'Invalid username or password!'})



       return render(request, 'users/login.html')
def teacher_dashboard(request):
       user_id = request.session['user_id']
       courses = Courses.objects.filter(teacher_id=user_id)
       return render(request, 'users/teacher_dashboard.html', {'courses': courses})



def student_dashboard(request):

      user_id = request.session['user_id']
      enrollments = Enrollment.objects.filter(student_id=user_id)
      return render(request, 'users/student_dashboard.html', {'enrollments': enrollments})
