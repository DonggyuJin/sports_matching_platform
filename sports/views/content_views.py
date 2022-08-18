from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..forms import ContentForm
from ..models import FreeContent

@login_required(login_url='common:login')
def content_create(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.author = request.user
            content.create_date = timezone.now()
            content.save()
            return redirect('sports:index')
    else:
        form = ContentForm()
    context = {'form': form}
    return render(request, 'sports/freeContent_form.html', context)

@login_required(login_url='common:login')
def content_modify(request, freeContent_id):
    freeContent = get_object_or_404(FreeContent, pk=freeContent_id)
    if request.user != freeContent.author:
        messages.error(request, '수정 권한이 없습니다!')
        return redirect('sports:detail', freeContent_id=freeContent.id)
    if request.method == "POST":
        form = ContentForm(request.POST, instance=freeContent)
        if form.is_valid():
            content = form.save(commit=False)
            content.modify_date = timezone.now()
            content.save()
            return redirect('sports:detail', freeContent_id=content.id)
    else:
        form = ContentForm(instance=freeContent)
    context = {'form': form}
    return render(request, 'sports/freeContent_form.html', context)

@login_required(login_url='common:login')
def content_delete(request, freeContent_id):
    freeContent = get_object_or_404(FreeContent, pk=freeContent_id)
    if request.user != freeContent.author:
        messages.error(request, '삭제 권한이 없습니다!')
        return redirect('sports:detail', freeContent_id=freeContent.id)
    freeContent.delete()
    return redirect('sports:index')

