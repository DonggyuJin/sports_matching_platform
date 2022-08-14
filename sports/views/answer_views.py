from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from ..models import FreeContent

def answer_create(request, freeContent_id):
    freeContent = get_object_or_404(FreeContent, pk=freeContent_id)
    freeContent.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('sports:detail', freeContent_id=freeContent.id)

