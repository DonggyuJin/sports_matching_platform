from django.contrib import admin

from .models import MatchSports


class MatchSportsAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(MatchSports, MatchSportsAdmin)