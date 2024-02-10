from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Language, Question, Answer

def index(request):
    languages = Language.objects.all()
    return render(request, 'index.html', {'languages': languages})

def add_language(request):
    if request.method == 'POST':
        language_name = request.POST.get('language_name')
        Language.objects.create(name=language_name)
        return HttpResponse('Language added successfully!')
    else:
        return HttpResponse('Invalid request method!')

def add_question_answer(request):
    if request.method == 'POST':
        language_id = request.POST.get('language')
        question_text = request.POST.get('question_text')
        answer_text = request.POST.get('answer_text')
        
        language = Language.objects.get(id=language_id)
        question = Question.objects.create(language=language, question_text=question_text)
        Answer.objects.create(question=question, answer_text=answer_text)
        
        return HttpResponse('Question and Answer added successfully!')
    else:
        return HttpResponse('Invalid request method!')

