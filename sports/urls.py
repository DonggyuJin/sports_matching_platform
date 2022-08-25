from django.urls import path

from .views import base_views, answer_views, content_views

app_name = 'sports'

urlpatterns = [
    # base_views
    path('', base_views.index, name='index'),
    path('<int:freeContent_id>', base_views.detail, name='detail'),
    
    # answer_views
    path('answer/create/<int:freeContent_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('answer/recommend/<int:answer_id>/', answer_views.answer_recommend, name='answer_recommend'),

    # content_views
    path('content/create/', content_views.content_create, name='content_create'),
    path('content/modify/<int:freeContent_id>/', content_views.content_modify, name='content_modify'),
    path('content/delete/<int:freeContent_id>/', content_views.content_delete, name='content_delete'),
    path('content/recommend/<int:freeContent_id>/', content_views.content_recommend, name='content_recommend'),
]