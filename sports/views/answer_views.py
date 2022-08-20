from turtle import title
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from ..models import FreeContent, FreeAnswer
from ..forms import AnswerForm

@login_required(login_url='common:login')
def answer_create(request, freeContent_id):
    freeContent = get_object_or_404(FreeContent, pk=freeContent_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.title = freeContent
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('sports:detail', freeContent_id=freeContent.id), answer.id))
    else:
        return HttpResponseNotAllowed('Post만 가능합니다.')
    context = {'freeContent': freeContent, 'form': form}
    return render(request, 'sports/freeContent_detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(FreeAnswer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('sports:detail', freeContent_id=answer.title.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('sports:detail', freeContent_id=answer.title.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'sports/freeContent_answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(FreeAnswer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('sports:detail', freeContent_id=answer.title.id)

@login_required(login_url='common:login')
def answer_recommend(request, answer_id):
    answer = get_object_or_404(FreeAnswer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 답변은 추천할수 없습니다')
    else:
        answer.recommend.add(request.user)
    return redirect('{}#answer_{}'.format(
                resolve_url('sports:detail', freeContent_id=answer.title.id), answer.id))


