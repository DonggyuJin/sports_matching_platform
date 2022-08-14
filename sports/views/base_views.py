from django.shortcuts import render, get_object_or_404

from ..models import FreeContent

def index(request):
    freeContent_list = FreeContent.objects.order_by('-create_date')
    context = {'freeContent_list': freeContent_list}
    return render(request, 'sports/freeContent_list.html', context)


def detail(request, freeContent_id):
    freeContent = get_object_or_404(FreeContent, pk=freeContent_id)
    context = {'freeContent': freeContent}
    return render(request, 'sports/freeContent_detail.html', context)
