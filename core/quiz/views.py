from django.shortcuts import redirect, render
from quiz.models import Quiz, QuizAttempt
# Create your views here.
from django.conf import settings
from groq import Groq
import json
from django.http import HttpResponse
def add_quiz(request,lesson_id):
     if request.method == 'POST':
        question_text = request.POST.get('question_text')
        option_a = request.POST.get('option_a')
        option_b = request.POST.get('option_b')
        option_c = request.POST.get('option_c')
        option_d = request.POST.get('option_d')
        correct_option = request.POST.get('correct_option')

        Quiz.objects.create(
            question_text=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_option=correct_option,
            lesson_id=lesson_id
        )
        return redirect('teacher_dashboard')

     return render(request, 'quiz/add_quiz.html')
def take_quiz(request, lesson_id):
     questions = Quiz.objects.filter(lesson_id=lesson_id)
    
     if request.method == 'POST':
        score = 0
        for question in questions:
            selected = request.POST.get(f'question_{question.id}')
            is_correct = selected == question.correct_option
            if is_correct:
                score += 1
            QuizAttempt.objects.create(
                student_id=request.session['user_id'],
                quiz_id=question.id,
                selected_option=selected,
                is_correct=is_correct
            )
        return render(request, 'quiz/result.html', {'score': score, 'total': questions.count()})
     return render(request, 'quiz/take_quiz.html', {'questions': questions})
 


def ai_generate_quiz(request, lesson_id):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        
        # Groq API call
        client = Groq(api_key=settings.GROQ_API_KEY)
        
        response = client.chat.completions.create(
            model= "llama-3.3-70b-versatile",
            messages=[{
                "role": "user",
                "content": f"""Generate 3 MCQ questions about '{topic}'.
                Return ONLY a JSON array like this:
                [
                    {{
                        "question": "Question here?",
                        "option_a": "Option A",
                        "option_b": "Option B", 
                        "option_c": "Option C",
                        "option_d": "Option D",
                        "correct_option": "A"
                    }}
                ]"""
            }]
        )
        
        # AI ka jawab parse karo
        content = response.choices[0].message.content
        questions = json.loads(content)
        
        # Database mein save karo
        for q in questions:
            Quiz.objects.create(
                question_text=q['question'],
                option_a=q['option_a'],
                option_b=q['option_b'],
                option_c=q['option_c'],
                option_d=q['option_d'],
                correct_option=q['correct_option'],
                lesson_id=lesson_id
            )
        
        return redirect('teacher_dashboard')
    
    return render(request, 'quiz/ai_generate.html')