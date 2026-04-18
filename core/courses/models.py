
from django.db import models

from users.models import User


# Create your models here.
class Courses(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
  
    created_at = models.DateTimeField(auto_now_add=True)
# Matlab: "ye course kisi User (teacher) ka hai"
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
class Lesson(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)



class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)