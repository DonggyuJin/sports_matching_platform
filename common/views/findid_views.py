from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
 
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
 
def findid(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        last_name = request.POST.get('last_name')
        chk_user = User.objects.get(email=email)
        print(chk_user.last_name)
        try:
            if chk_user==User.objects.get(last_name=last_name):
                print(User.objects.get(email=email))
                return HttpResponse("%s" %chk_user.username)
        except:
            return HttpResponse('''<script>alert("일치하는 정보가 없습니다.");history.go(-1);</script>''')
    return render(request, 'common/findid.html')
