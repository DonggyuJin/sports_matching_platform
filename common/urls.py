from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from .views import signup_views, index_views, profile_views, ranking_views

app_name = 'common'

urlpatterns = [
    path('', index_views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_views.signup, name='signup'),
    path('profile/base/<int:user_id>/', profile_views.profile_base, name='profile_base'),

    # 아이디 찾기
    path('recovery/id/', profile_views.RecoveryIdView.as_view(), name='recovery_id'),
    path('recovery/id/find/', profile_views.ajax_find_id_view, name='ajax_id'),

    # 비밀번호 찾기
    path('recovery/pw/', profile_views.RecoveryPwView.as_view(), name='recovery_pw'),
    path('recovery/pw/find/', profile_views.ajax_find_pw_view, name='ajax_pw'),
    path('recovery/pw/auth/', profile_views.auth_confirm_view, name='recovery_auth'),
    path('recovery/pw/reset/', profile_views.auth_pw_reset_view, name='recovery_pw_reset'),

    # 프로필 수정
    path('profile/update/<int:user_id>/', profile_views.profile_update_view, name='profile_update'),
    path('profile/change_password/<int:user_id>', profile_views.password_edit_view, name='password_edit'),

    # 랭킹
    path('ranking/', ranking_views.ranking, name='ranking')
]