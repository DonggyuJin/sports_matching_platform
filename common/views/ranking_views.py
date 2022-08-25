from common.models import CustomUser
from django.shortcuts import render, get_object_or_404

def ranking(request):
    user_ranking = CustomUser.objects.order_by('-score')
    print(len(user_ranking))
    return render(request, 'ranking/ranking.html', {'user_ranking': user_ranking, 'index': 0})