from django import forms
from django.contrib.auth.models import User
from qa.models import Question,Answer

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

       
class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def login(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()    

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget = forms.Textarea)
    
    
    def save(self):
        self.cleaned_data['author'] = self._user
        quest = Question(**self.cleaned_data)
        quest.save()
        return quest

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=1000)
    question = forms.ModelChoiceField(queryset=Question.objects.all(),
        widget=forms.HiddenInput()) 
    def save(self):       
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

