from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

class FAQAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq1 = FAQ.objects.create(
            question="What are the key features of Django?",
            answer="Django's key features include an ORM for database interactions, a powerful admin interface, URL routing, template engine, form handling, authentication system, caching, and built-in security features like protection against CSRF, XSS, and SQL injection.",
            question_hi="जांगो की प्रमुख विशेषताएं क्या हैं?",
            answer_hi="जांगो की प्रमुख विशेषताओं में डेटाबेस इंटरैक्शन के लिए ORM, एक शक्तिशाली एडमिन इंटरफ़ेस, URL राउटिंग, टेम्पलेट इंजन, फॉर्म हैंडलिंग, प्रमाणीकरण प्रणाली, कैशिंग और CSRF, XSS और SQL इंजेक्शन से सुरक्षा जैसी अंतर्निहित सुरक्षा सुविधाएं शामिल हैं।",
            question_bn="Django-এর মূল বৈশিষ্ট্যগুলি কী কী?",
            answer_bn="Django-এর মূল বৈশিষ্ট্যগুলির মধ্যে রয়েছে ডাটাবেস ইন্টারঅ্যাকশনের জন্য একটি ORM, একটি শক্তিশালী অ্যাডমিন ইন্টারফেস, URL রাউটিং, টেমপ্লেট ইঞ্জিন, ফর্ম হ্যান্ডলিং, অথেনটিকেশন সিস্টেম, ক্যাশিং এবং CSRF, XSS এবং SQL ইনজেকশনের বিরুদ্ধে সুরক্ষার মতো অন্তর্নির্মিত নিরাপত্তা বৈশিষ্ট্য।"
        )
        self.faq2 = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the model-template-view (MTV) architectural pattern and includes an ORM, authentication system, and admin interface out of the box.",
            question_hi="जांगो क्या है?",
            answer_hi="जांगो एक उच्च-स्तरीय पायथन वेब फ्रेमवर्क है जो तेज़ विकास और स्वच्छ, व्यावहारिक डिज़ाइन को प्रोत्साहित करता है। यह मॉडल-टेम्पलेट-व्यू (MTV) आर्किटेक्चरल पैटर्न का पालन करता है और इसमें ORM, प्रमाणीकरण प्रणाली और एडमिन इंटरफ़ेस शामिल हैं।",
            question_bn="Django কী?",
            answer_bn="Django একটি উচ্চ-স্তরের Python ওয়েব ফ্রেমওয়ার্ক যা দ্রুত উন্নয়ন এবং পরিষ্কার, প্র্যাগম্যাটিক ডিজাইনকে উৎসাহিত করে। এটি মডেল-টেমপ্লেট-ভিউ (MTV) আর্কিটেকচারাল প্যাটার্ন অনুসরণ করে এবং এর মধ্যে ORM, অথেনটিকেশন সিস্টেম এবং অ্যাডমিন ইন্টারফেস রয়েছে।"
        )
        self.faq3 = FAQ.objects.create(
            question="What payment methods do you accept?",
            answer="We accept all major credit cards (Visa, Mastercard, American Express), PayPal, and bank transfers.",
            question_hi="आप कौन से भुगतान विधियों को स्वीकार करते हैं?",
            answer_hi="हम सभी प्रमुख क्रेडिट कार्ड (वीसा, मास्टरकार्ड, अमेरिकन एक्सप्रेस), पेपाल और बैंक ट्रांसफर स्वीकार करते हैं।",
            question_bn="আপনি কোন পেমেন্ট পদ্ধতি গ্রহণ করেন?",
            answer_bn="আমরা সমস্ত প্রধান ক্রেডিট কার্ড (ভিসা, মাস্টারকার্ড, আমেরিকান এক্সপ্রেস), পেপাল এবং ব্যাংক ট্রান্সফার গ্রহণ করি।"
        )

    def test_faq_list(self):
        response = self.client.get(reverse('faq-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_faq_detail(self):
    # Fetch the FAQ entries by their primary keys
        faq1 = FAQ.objects.get(pk=1)
        faq3 = FAQ.objects.get(pk=3)

        # Test for FAQ with pk=1
        response = self.client.get(reverse('faq-detail', kwargs={'pk': faq1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['question'], faq1.question)

        # Test for FAQ with pk=3
        response = self.client.get(reverse('faq-detail', kwargs={'pk': faq3.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['question'], faq3.question)

    def test_faq_content(self):
        response = self.client.get(reverse('faq-list'))
        self.assertEqual(response.status_code, 200)
        questions = [faq['question'] for faq in response.data]
        self.assertEqual(questions, [
            "What are the key features of Django?",
            "What is Django?",
            "What payment methods do you accept?"
        ])

    def test_faq_language_support(self):
        response = self.client.get(reverse('faq-list') + '?lang=hi')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['question'], "जांगो की प्रमुख विशेषताएं क्या हैं?")
        self.assertEqual(response.data[1]['question'], "जांगो क्या है?")
        self.assertEqual(response.data[2]['question'], "आप कौन से भुगतान विधियों को स्वीकार करते हैं?")

        response = self.client.get(reverse('faq-list') + '?lang=bn')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['question'], "Django-এর মূল বৈশিষ্ট্যগুলি কী কী?")
        self.assertEqual(response.data[1]['question'], "Django কী?")
        self.assertEqual(response.data[2]['question'], "আপনি কোন পেমেন্ট পদ্ধতি গ্রহণ করেন?")
