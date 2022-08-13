from django.shortcuts import render

from .models import freeBoard_content

def index(request):
    freeContent_list = freeBoard_content.objects.order_by('-create_date')
    context = {'freeContent_list': freeContent_list}
    return render(request, 'sports/freeContent_list.html', context)