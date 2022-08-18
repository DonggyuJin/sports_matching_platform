from django import forms
from sports.models import FreeContent, FreeAnswer


class ContentForm(forms.ModelForm):
    class Meta:
        model = FreeContent 
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = FreeAnswer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
