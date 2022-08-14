from django.urls import path
from django.contrib.auth import views as auth_views

from .views import index_views

app_name = 'common'

urlpatterns = [
    path('', index_views.index, name='index'),
]