from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Article
from django.http import HttpResponse

@require_GET
def test(request, *args, **kwargs):   
    article = get_object_or_404(Article, id = 1)
    return render(request, "qa/index.html",{'article': article})    
#return HttpResponse('OK')
