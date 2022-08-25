from django.db.models import F, Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from common.models import CustomUser
from common.forms import CustomUserChangeForm, CustomPasswordChangeForm, RecoveryIdForm, RecoveryPwForm, CustomSetPasswordForm
import json
from django.core.serializers.json import DjangoJSONEncoder
from common.helper import email_auth_num, send_mail
from django.template.loader import render_to_string
from django.core.exceptions import PermissionDenied

def ajax_find_pw_view(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    target_user = CustomUser.objects.get(username=username, email=email)

    if target_user:
        auth_num = email_auth_num()
        target_user.auth = auth_num 
        target_user.save()

        send_mail(
            '비밀번호 찾기 인증메일입니다.',
            [email],
            html=render_to_string('common/recovery_email.html', {
                'auth_num': auth_num,
            }),
        )
    return HttpResponse(json.dumps({"result": target_user.username}, cls=DjangoJSONEncoder), content_type = "application/json")

def ajax_find_id_view(request):
    email = request.POST.get('email')
    result_id = CustomUser.objects.get(email=email)
       
    return HttpResponse(json.dumps({"result_id": result_id.username}, cls=DjangoJSONEncoder), content_type = "application/json")

# 프로필 메인화면
def profile_base(request, user_id):

    user = get_object_or_404(CustomUser, pk=user_id)
    context = {'profile_user': user, 'profile_type': 'base'}
    return render(request, 'common/profile/profile_base.html', context)

# 아이디 찾기
class RecoveryIdView(View):
    template_name = 'common/recovery_id.html'
    recovery_id = RecoveryIdForm
    def get(self, request):
        if request.method=='GET':
            form_id = self.recovery_id(None)
        return render(request, self.template_name, { 'form_id':form_id, })

# 비밀번호 찾기
class RecoveryPwView(View):
    template_name = 'common/recovery_pw.html'
    recovery_pw = RecoveryPwForm

    def get(self, request):
        if request.method=='GET':
            form = self.recovery_pw(None)
            return render(request, self.template_name, { 'form':form, })

def auth_confirm_view(request):
    username = request.POST.get('username')
    input_auth_num = request.POST.get('input_auth_num')
    target_user = CustomUser.objects.get(username=username, auth=input_auth_num)
    target_user.auth = ""
    target_user.save()
    request.session['auth'] = target_user.username
    
    return HttpResponse(json.dumps({"result": target_user.username}, cls=DjangoJSONEncoder), content_type = "application/json")

def auth_pw_reset_view(request):
    if request.method == 'GET':
        if not request.session.get('auth', False):
            raise PermissionDenied

    if request.method == 'POST':
        session_user = request.session['auth']
        current_user = CustomUser.objects.get(username=session_user)
        login(request, current_user)

        reset_password_form = CustomSetPasswordForm(request.user, request.POST)
        
        if reset_password_form.is_valid():
            user = reset_password_form.save()
            messages.success(request, "비밀번호 변경완료! 변경된 비밀번호로 로그인하세요.")
            logout(request)
            return redirect('common:login')
        else:
            logout(request)
            request.session['auth'] = session_user
    else:
        reset_password_form = CustomSetPasswordForm(request.user)

    return render(request, 'common/password_reset.html', {'form':reset_password_form})

# 비밀번호 수정
def password_edit_view(request, user_id):
    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호를 성공적으로 변경하였습니다.")
            return redirect('common:profile_base', user_id=user.id)
    else:
        password_change_form = CustomPasswordChangeForm(request.user)

    return render(request, 'common/profile/profile_password.html', {'password_change_form':password_change_form})


# 프로필 수정
def profile_update_view(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(CustomUser, pk=user_id)
        user_change_form = CustomUserChangeForm(request.POST, instance = request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return redirect('common:profile_base', user_id=user.id)
    else:
        user_change_form = CustomUserChangeForm(instance = request.user)

        return render(request, 'common/profile/profile_update.html', {'user_change_form':user_change_form})
