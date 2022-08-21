from django.shortcuts import render, get_object_or_404

from ..models import MatchSports

def index(request):
    match_list = MatchSports.objects.order_by('-create_date')
    context = {'match_list': match_list}
    return render(request, 'match/match_list.html', context)

def detail(request, match_id):
    match_content = get_object_or_404(MatchSports, pk=match_id)
    context = {'match_content': match_content}
    return render(request, 'match/match_detail.html', context)