from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def test(request, *args, **kwargs):   
    return render(request, 'index.html')    
#return HttpResponse('OK')
