from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET,require_POST
from qa.models import Article, Question,Answer
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from qa.forms import AskForm,AnswerForm, SignUpForm, LoginForm
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = SignUpForm()
    return render(request, "qa/register.html", {
        'form' : form,
    })
@require_GET
def test(request, *args, **kwargs):   
    article = get_object_or_404(Article, id = 1)
    return render(request, "qa/index.html",{'article': article})    
#return HttpResponse('OK')

def mylogin(request):
    message = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                message = 'username or password are incorrect'
    else:
        form = LoginForm()
    return render(request, 'qa/login.html',{
        'form': form,
        'message':message,
    })
            
                   
def quest_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            quest = form.save()
            return HttpResponseRedirect('/question/' + str(quest.id)+'/')
    else:
        form = AskForm()
    return render(request, 'qa/quest_add.html',{
        'form' : form
    })

@require_GET
def question_detail(request,id):   
    quest = get_object_or_404(Question, id = id)
    answers = Answer.objects.all().filter(question_id = id)[:]
    answer_form = AnswerForm(initial={'question': quest})
    return render(request, 'qa/question_detail.html', {
        'quest': quest,
        'answers': answers,
        'answer_form': answer_form
    })
@require_POST
def answer_add(request):
    answer_form = AnswerForm(request.POST)
    answer_form._user = request.user
    if answer_form.is_valid():
        answer = answer_form.save()        
    quest_id = request.POST['question']    
    return HttpResponseRedirect(reverse('question', args=[quest_id])) 

      
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
    
