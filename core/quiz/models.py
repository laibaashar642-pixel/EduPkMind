
from django.db import models
from courses.models import Lesson
from users.models import User
# Create your models here.
class Quiz(models.Model):
       question_text=models.CharField(max_length=100)
       option_a=models.CharField(max_length=100)
       option_b=models.CharField(max_length=100)
       option_c=models.CharField(max_length=100)
       option_d=models.CharField(max_length=100)
       correct_option=models.CharField(max_length=100)
      
       lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class QuizAttempt(models.Model):
        student = models.ForeignKey(User, on_delete=models.CASCADE)
        quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
        selected_option = models.CharField(max_length=1)
        is_correct = models.BooleanField(default=False)
        attempted_at = models.DateTimeField(auto_now_add=True)

