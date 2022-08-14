from django.urls import path

from .views import base_views, answer_views

app_name = 'sports'

urlpatterns = [
    # base_views
    path('', base_views.index, name='index'),
    path('<int:freeContent_id>', base_views.detail, name='detail'),
    
    # answer_views
    path('answer/create/<int:freeContent_id>/', answer_views.answer_create, name='answer_create'),
]
