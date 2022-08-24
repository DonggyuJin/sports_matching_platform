from django.urls import path

from .views import base_views, match_views

app_name = 'match'

urlpatterns = [
    # base_views
    path('', base_views.index, name='index'),
    path('<int:match_id>/', base_views.detail, name='detail'),
    path('<int:match_id>/match/', base_views.match_apply, name='apply'),

    # match_views
    path('match/create/', match_views.match_create, name='match_create'),
    path('match/modify/<int:match_id>/', match_views.match_modify, name='match_modify'),
    path('match/delete/<int:match_id>/', match_views.match_delete, name='match_delete'),

]