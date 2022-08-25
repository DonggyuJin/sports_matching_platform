from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import MatchSports

def review_index(request):
    match_list = MatchSports.objects.order_by('-create_date')
    for review in match_list:
        if review.max_apply == review.apply_count:
            print(review)
            return render(HTTPResponse('hi'))
    context = {'match_list': match_list}
    return render(request, 'match/match_list.html', context)

# def detail(request, match_id):
#     match_content = get_object_or_404(MatchSports, pk=match_id)
#     context = {'match_content': match_content}
#     return render(request, 'match/match_detail.html', context)
