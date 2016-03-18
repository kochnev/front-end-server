from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Article, Question
from django.http import HttpResponse

@require_GET
def test(request, *args, **kwargs):   
    article = get_object_or_404(Article, id = 1)
    return render(request, "qa/index.html",{'article': article})    
#return HttpResponse('OK')

@require_GET
def question_list_all(request, page):
    q_list = Question.objects.order_by('-id')
    
    return render(requestn, 'qa/index.html', {
       'q_list':q_list[0:10]
    }) 

