from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.utils.translation import get_language
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from rest_framework.response import Response

@method_decorator(cache_page(60 * 15), name='dispatch')
class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', get_language())
        return FAQ.objects.all().order_by('question')

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faq_list_{lang}'
        
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
        
        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=60*15)
        return response
