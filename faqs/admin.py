from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'get_answer_preview')
    search_fields = ('question', 'answer')

    def get_answer_preview(self, obj):
        return obj.answer[:50] + '...' if len(obj.answer) > 50 else obj.answer
    get_answer_preview.short_description = 'Answer Preview'
