from django.contrib import admin
from .models import freeBoard_content, freeBoard_answer


class freeBoard_contentAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(freeBoard_answer)
admin.site.register(freeBoard_content, freeBoard_contentAdmin)

