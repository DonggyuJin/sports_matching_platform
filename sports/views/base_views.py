from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator 

from ..models import FreeContent

def index(request):
    freeContent_list = FreeContent.objects.order_by('-create_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(freeContent_list, 10)
    page_obj = paginator.get_page(page)
    context = {'freeContent_list': page_obj}
    return render(request, 'sports/freeContent_list.html', context)


def detail(request, freeContent_id):
    freeContent = get_object_or_404(FreeContent, pk=freeContent_id)
    context = {'freeContent': freeContent}
    return render(request, 'sports/freeContent_detail.html', context)
