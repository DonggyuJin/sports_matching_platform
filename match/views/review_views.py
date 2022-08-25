from difflib import Match
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import MatchSports

@login_required(login_url='common:login')
def review_index(request):
    review_list = MatchSports.objects.order_by('-create_date')
    context = {'review_list': review_list}
    return render(request, 'match/review_list.html', context)

# def detail(request, match_id):
#     match_content = get_object_or_404(MatchSports, pk=match_id)
#     context = {'match_content': match_content}
#     return render(request, 'match/match_detail.html', context)
