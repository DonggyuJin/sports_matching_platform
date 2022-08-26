from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from common.models import CustomUser
from ..models import MatchSports, UserApply

# 후기 게시판 (마감된 글 중 자신이 신청한 글과 자신이 작성한 글 표시)
@login_required(login_url='common:login')
def review_index(request):
    matchapply = MatchSports.objects.order_by('-create_date')
    userapply = UserApply.objects.filter(user_check=request.user)
    user = CustomUser.objects.get(username=request.user)
    match_list = []
    print(user.id)
    for i in range(len(userapply)):
        for j in range(len(matchapply)):
            if matchapply[j].max_apply == matchapply[j].apply_count:
                if userapply[i].match_check == matchapply[j].id:
                    match_list.append(matchapply[j])

    for k in range(len(matchapply)):
        if matchapply[k].max_apply == matchapply[k].apply_count:
            if matchapply[k].author_id == user.id:
                match_list.append(matchapply[k])
        

    context = {'match_list': match_list}
    return render(request, 'match/match_review.html', context)


@login_required(login_url='common:login')
def review_detail(request, match_id):
    userapply = UserApply.objects.filter(match_check=match_id)
    user_list = []
    for i in range(len(userapply)):
        user = CustomUser.objects.get(username=userapply[i].user_check)
        user_list.append(user)
    print(user_list)
    matchapply = get_object_or_404(MatchSports, pk=match_id)
    print(matchapply.author.username)
    if request.method == "POST":
        for j in range(len(user_list)):
            score = request.POST.get(f'score{j}')
            score_author = request.POST.get('score')
            user1 = CustomUser.objects.get(username=user_list[j].username)
            user3 = CustomUser.objects.get(username=matchapply.author.username)
            if score_author == '2':
                user3.score += 2
            elif score_author == '1':
                user3.score += 1
            else :
                user3.score += 0

            if score == '2':
                user1.score += 2
            elif score == '1':
                user1.score += 1
            else :
                user1.score += 0
            user1.save()
            user3.save()
        user2 = UserApply.objects.get(match_check=match_id, user_check=request.user)
        user2.delete()
        return HttpResponse('''<script>alert("후기작성이 완료되었습니다."); window.location.href="/match/review";</script>''')
    else: 
        context = {'userapply': userapply, 'matchapply': matchapply, 'user': user_list}
        return render(request, 'match/review_detail.html', context)

# def detail(request, match_id):
#     match_content = get_object_or_404(MatchSports, pk=match_id)
#     context = {'match_content': match_content}
#     return render(request, 'match/match_detail.html', context)
