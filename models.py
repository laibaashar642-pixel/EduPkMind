from django.db import models

# Create your models here.
class User(models.Model):

      TEACHER = 'teacher'
      STUDENT = 'student'
    
      ROLE_CHOICES = [
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    ]
    
      username=models.CharField(max_length=100),
      email=models.EmailField(),
      password=models.CharField(max_length=100),
      role=models.CharField(max_length=20, choices=ROLE_CHOICES),
      profile_picture=models.ImageField(),
