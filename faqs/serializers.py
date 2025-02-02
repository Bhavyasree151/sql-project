from rest_framework import serializers
from .models import FAQ
from django.conf import settings

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def get_language_field(self, obj, field_name, lang):
        supported_languages = [code for code, name in settings.LANGUAGES]
        if lang in supported_languages:
            return getattr(obj, f'{field_name}_{lang}', getattr(obj, field_name))
        return getattr(obj, field_name)

    def get_question(self, obj):
        lang = self.context['request'].query_params.get('lang', 'en')
        return self.get_language_field(obj, 'question', lang)

    def get_answer(self, obj):
        lang = self.context['request'].query_params.get('lang', 'en')
        return self.get_language_field(obj, 'answer', lang)
