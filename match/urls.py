from django.urls import path

from .views import base_views

app_name = 'match'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:match_id>/', base_views.detail, name='detail'),
]