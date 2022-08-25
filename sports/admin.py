from django.contrib import admin
from .models import FreeContent, FreeAnswer


class FreeContentAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(FreeAnswer)
admin.site.register(FreeContent, FreeContentAdmin)

