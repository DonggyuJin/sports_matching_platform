from django import forms
from match.models import MatchSports


class MatchForm(forms.ModelForm):
    class Meta:
        model = MatchSports 
        fields = ['title', 'sports_name', 'sports_date', 'address', 'max_apply', 'content']
        labels = {
            'title': '제목',
            'sports_name': '스포츠명',
            'sports_date': '일정',
            'address': '주소',
            'max_apply': '최대신청인원',
            'content': '내용',
        }

