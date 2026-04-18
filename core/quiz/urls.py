from django.urls import path
from .views import add_quiz, take_quiz,ai_generate_quiz
urlpatterns=[
      path('add/<int:lesson_id>/', add_quiz, name='add_quiz'),
      path('take/<int:lesson_id>/', take_quiz, name='take_quiz'),
      path('ai-generate/<int:lesson_id>/', ai_generate_quiz, name='ai_generate_quiz'),
]