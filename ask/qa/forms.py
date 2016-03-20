from django import forms
from qa.models import Question,Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget = forms.Textarea)
    
    def save(self):
        quest = Question(**self.cleaned_data)
        quest.save()
        return quest

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=1000)
    question = forms.ModelChoiceField(queryset=Question.objects.all(),
        widget=forms.HiddenInput()) 
    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

