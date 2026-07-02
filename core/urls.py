from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('consultation/', views.consultation_view, name='consultation'),
    path('news/', views.news_view, name='news'),
    path('downloads/', views.downloads_view, name='downloads'),
    path('faq/', views.faq_view, name='faq'),
]
