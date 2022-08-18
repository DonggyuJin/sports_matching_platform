from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            origin_password = form.cleaned_data.get('password1')
            # 사용자 인증을 진행하는 부분으로
            # django.contrib.auth.authenticate가 검증한다.
            user = authenticate(username=username, password=origin_password)
            # django.contrib.auth.login으로 로그인하여 세션을 생성한다.
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})