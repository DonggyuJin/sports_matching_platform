from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_views

from .views import index_views

app_name = 'common'

urlpatterns = [
    path('', index_views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_views.signup, name='signup')
]