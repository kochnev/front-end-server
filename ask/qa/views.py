from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Article, Question,Answer
from django.http import HttpResponse
from django.core.paginator import Paginator

@require_GET
def test(request, *args, **kwargs):   
    article = get_object_or_404(Article, id = 1)
    return render(request, "qa/index.html",{'article': article})    
#return HttpResponse('OK')


def question_detail(request):
  #  id = args[0]
    return HttpResponse('OK2')
  #  quest = get_object_or_404(Question, id = id)
  #  answers = Answer.objects.all().filter(question_id = id)[:]
  #  return render(request, 'qa/question_detail.html', {
  #      'quest': quest,
  #      'answers': answers
  #  })
@require_GET
def main(request, page = None):
    try:
        limit = int(request.GET.get('limit', 10))
    except:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    paginator = Paginator(Question.objects.all().order_by('-id'), limit)
    paginator.baseurl = '/?page='
    quests = paginator.page(page)
    
    return render(request, "qa/index.html", {
        'all_quests': quests.object_list,
        'paginator': paginator,
        'page': quests,
    }) 
 #   return HttpResponse('OKsdfsdfq')
@require_GET
def popular(request, page = None):
    try:
        limit = int(request.GET.get('limit', 10))
    except:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    paginator = Paginator(Question.objects.all().order_by('-rating'), limit)
    paginator.baseurl = '/popular/?page='
    quests = paginator.page(page)
    
    return render(request, "qa/index.html", {
        'all_quests': quests.object_list,
        'paginator': paginator,
        'page': quests,
    }) 
    
