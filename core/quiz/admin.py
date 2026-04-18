from django.contrib import admin

# Register your models here.
from quiz.models import Quiz,QuizAttempt
admin.site.register(Quiz)
admin.site.register(QuizAttempt)