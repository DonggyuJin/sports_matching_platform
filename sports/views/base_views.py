from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from ..models import FreeContent, FreeAnswer

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
    # 답변 페이징을 위한 list
    answer_list = FreeAnswer.objects.filter(title_id=freeContent_id).order_by('create_date')
    answer_page = request.GET.get('page', '1')
    answer_paginator = Paginator(answer_list, 5)
    answer_page_obj = answer_paginator.get_page(answer_page)
    # answer_list에 답변 페이징 객체 전달
    context = {'freeContent': freeContent, 'answer_list': answer_page_obj, 'page': answer_page}
    return render(request, 'sports/freeContent_detail.html', context)
