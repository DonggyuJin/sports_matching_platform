from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from ..models import FreeContent

def index(request):
    freeContent_list = FreeContent.objects.order_by('-create_date')
    page = request.GET.get('page', 1)
    sports = request.GET.get('sports', '')
    if sports:
        # 검색 기능
        freeContent_list = freeContent_list.filter(
            # contains가 아닌 icontains를 사용하는 이유는
            # icontains는 대소문자를 가리지 않고 검색이 가능하다.
            Q(subject__icontains=sports) |  # 제목
            Q(content__icontains=sports) |  # 내용
            Q(freeanswer__content__icontains=sports) |  # 답변 내용
            Q(author__username__icontains=sports) |  # 질문 글쓴이
            Q(freeanswer__author__username__icontains=sports)  # 답변 글쓴이
        ).distinct()
    paginator = Paginator(freeContent_list, 10)
    page_obj = paginator.get_page(page)
    context = {'freeContent_list': page_obj, 'page': page, 'sports': sports}
    return render(request, 'sports/freeContent_list.html', context)


def detail(request, freeContent_id):
    freeContent = get_object_or_404(FreeContent, pk=freeContent_id)
    context = {'freeContent': freeContent}
    return render(request, 'sports/freeContent_detail.html', context)
