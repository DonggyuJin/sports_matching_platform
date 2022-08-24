from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..forms import MatchForm
from ..models import MatchSports

@login_required(login_url='common:login')
def match_create(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            match_content = form.save(commit=False)
            match_content.author = request.user
            match_content.create_date = timezone.now()
            match_content.save()
            return redirect('match:index')
    else:
        form = MatchForm()
    context = {'form': form}
    return render(request, 'match/match_form.html', context)

@login_required(login_url='common:login')
def match_modify(request, match_id):
    match = get_object_or_404(MatchSports, pk=match_id)
    if request.user != match.author:
        messages.error(request, '수정 권한이 없습니다!')
        return redirect('match:index')
    if request.method == "POST":
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            match_content = form.save(commit=False)
            match_content.modify_date = timezone.now()
            match_content.save()
            return redirect('match:index')
    else:
        form = MatchForm(instance=match)
    context = {'form': form}
    return render(request, 'match/match_form.html', context)

@login_required(login_url='common:login')
def match_delete(request, match_id):
    match = get_object_or_404(MatchSports, pk=match_id)
    if request.user != match.author:
        messages.error(request, '삭제 권한이 없습니다!')
        return redirect('match:index')
    match.delete()
    return redirect('match:index')

