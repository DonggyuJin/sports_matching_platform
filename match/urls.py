from django.urls import path

from .views import base_views, match_views, review_views

app_name = 'match'

urlpatterns = [
    # base_views
    path('', base_views.index, name='index'),
    path('<int:match_id>/', base_views.detail, name='detail'),
    path('<int:match_id>/match/', base_views.match_apply, name='apply'),

    # match_views
    path('create/', match_views.match_create, name='match_create'),
    path('modify/<int:match_id>/', match_views.match_modify, name='match_modify'),
    path('delete/<int:match_id>/', match_views.match_delete, name='match_delete'),

    # review_views
    path('review/', review_views.review_index, name='review_index'),
    path('<int:match_id>/review/', base_views.review_apply, name='review_apply'),
    path('<int:match_id>/review/detail', review_views.review_detail, name='review_detail'),
]