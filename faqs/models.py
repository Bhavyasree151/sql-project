from django.db import models

# Create your models here.
# faqs/models.py

from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from google_trans_new import google_translator

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))
    question_hi = models.TextField(_("Question (Hindi)"), blank=True)
    question_bn = models.TextField(_("Question (Bengali)"), blank=True)
    answer_hi = RichTextField(_("Answer (Hindi)"), blank=True)
    answer_bn = RichTextField(_("Answer (Bengali)"), blank=True)

    def get_translated_field(self, field, lang):
        cache_key = f"faq_{self.id}_{field}_{lang}"
        cached_value = cache.get(cache_key)
        if cached_value:
            return cached_value

        if lang == 'en' or not hasattr(self, f"{field}_{lang}"):
            value = getattr(self, field)
        else:
            value = getattr(self, f"{field}_{lang}")
            if not value:
                translator = google_translator()
                value = translator.translate(getattr(self, field), lang_tgt=lang)
                setattr(self, f"{field}_{lang}", value)
                self.save()

        cache.set(cache_key, value, timeout=3600)  # Cache for 1 hour
        return value

    def get_question(self, lang='en'):
        return self.get_translated_field('question', lang)

    def get_answer(self, lang='en'):
        return self.get_translated_field('answer', lang)

    def __str__(self):
        return self.question
