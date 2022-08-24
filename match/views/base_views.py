from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models import MatchSports

def index(request):
    match_list = MatchSports.objects.order_by('-create_date')
    context = {'match_list': match_list}
    return render(request, 'match/match_list.html', context)

def detail(request, match_id):
    match_content = get_object_or_404(MatchSports, pk=match_id)
    context = {'match_content': match_content}
    return render(request, 'match/match_detail.html', context)

@login_required(login_url='common:login')
def match_apply(request, match_id):
    match = get_object_or_404(MatchSports, pk=match_id)
    if request.user != match.author:
        if request.user in match.apply_state.all():
            match.apply_state.remove(request.user)
            match.apply_count -=1
            match.save()
        else:
            match.apply_state.add(request.user)
            match.apply_count += 1
            match.save()
            return redirect('match:index')
    return redirect('match:index')
