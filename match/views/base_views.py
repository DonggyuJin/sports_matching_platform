from msilib.schema import CustomAction
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from common.models import CustomUser

from ..models import MatchSports, UserApply

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
    userapply = UserApply()
    if request.user != match.author:
        if request.user in match.apply_state.all():
            match.apply_state.remove(request.user)
            match.apply_count -=1
            userapply_delete = UserApply.objects.filter(match_check=match.id)
            userapply_delete.delete()
            userapply.save()
            match.save()
        else:
            match.apply_state.add(request.user)
            match.apply_count += 1
            userapply.user_check = request.user
            userapply.match_check = match.id
            match.save()
            userapply.save()
            return redirect('match:index')
    return redirect('match:index')

@login_required(login_url='common:login')
def review_apply(request, match_id):
    match = get_object_or_404(MatchSports, pk=match_id)
    userapply = UserApply()
    if request.user != match.author:
        if request.user in match.apply_state.all():
            match.apply_state.remove(request.user)
            match.apply_count -=1
            userapply_delete = UserApply.objects.filter(match_check=match.id)
            userapply_delete.delete()
            userapply.save()
            match.save()
        else:
            match.apply_state.add(request.user)
            match.apply_count += 1
            userapply.user_check = request.user
            userapply.match_check = match.id
            match.save()
            userapply.save()
            return redirect('match:review_index')
    return redirect('match:review_index')

