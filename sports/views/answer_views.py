from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required

from ..models import FreeContent, FreeAnswer
from ..forms import AnswerForm

@login_required(login_url='common:login')
def answer_create(request, answer_id):
    freeContent = get_object_or_404(FreeContent, pk=answer_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.title = freeContent
            answer.save()
            return redirect('sports:detail', answer_id=freeContent.id)
    else:
        return HttpResponseNotAllowed('Post만 가능합니다.')
    context = {'freeContent': freeContent, 'form': form}
    return render(request, 'sports/freeContent_detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    freeAnswer = get_object_or_404(FreeAnswer, pk=answer_id)

