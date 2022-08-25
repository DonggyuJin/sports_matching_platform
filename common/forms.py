from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm, SetPasswordForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["nickname", "username", "password1", "password2", "email", "phonenumber", "address", "favorite", "introduction"]
        labels = {
            'nickname': '닉네임',
            'username': '아이디',
            'password1': '비밀번호',
            'password2': '비밀번호 확인',
            'email': '이메일',
            'phonenumber': '핸드폰 번호',
            'address': '주소',
            'favorite': '선호하는 운동',
            'introduction': '자기소개'
        }

class RecoveryIdForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(RecoveryIdForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_email' 
        })

class RecoveryPwForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput,)
    email = forms.EmailField(
        widget=forms.EmailInput,)

    class Meta:
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(RecoveryPwForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_id',
        })
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_email',
        })

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })
        
class CustomUserChangeForm(UserChangeForm):
    password = None
    nickname = forms.CharField(label='닉네임', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'20', 'oninput':"maxLengthCheck(this)"}), 
    )        
    phonenumber = forms.CharField(label='핸드폰 번호', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'11', 'oninput':"maxLengthCheck(this)"}), 
    )        
    address = forms.CharField(label='학번', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'200', 'oninput':"maxLengthCheck(this)"}), 
    )
    favorite = forms.CharField(label='선호하는 운동', widget=forms.TextInput(
        attrs={'class': 'form-control','maxlength':'200', 'oninput':"maxLengthCheck(this)"}), 
    )
    introduction = forms.CharField(label='자기소개', widget=forms.TextInput(
        attrs={'class': 'form-control','maxlength':'200', 'oninput':"maxLengthCheck(this)"}), 
    )

    class Meta:
        model = CustomUser()
        fields = ['nickname', 'phonenumber', 'address', 'favorite', 'introduction']

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = '기존 비밀번호'
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False,
        })
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })