from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'base.html')

def signup(request):
     return render(request,'users/sign-up.html')
def login(request):
     if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username,password)
     
     
     return render(request,'users/login.html')