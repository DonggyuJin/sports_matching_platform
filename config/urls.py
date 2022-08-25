from django.contrib import admin
from django.urls import path, include

from common.views import index_views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # sports app
    path('', index_views.index, name='index'),
    path('sports/', include('sports.urls')),
    path('common/', include('common.urls')),
]
