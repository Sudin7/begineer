from django.contrib import admin
from .models import NewsItem, DownloadableFile, FAQItem, ConsultationRequest


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'is_published')
    list_filter = ('is_published', 'published_at')
    search_fields = ('title', 'summary', 'body')
    ordering = ('-published_at',)


@admin.register(DownloadableFile)
class DownloadableFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'uploaded_at')
    search_fields = ('title', 'description')
    ordering = ('-uploaded_at',)


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'preferred_date', 'preferred_time', 'created_at')
    list_filter = ('preferred_date',)
    search_fields = ('name', 'email', 'phone', 'message')
    ordering = ('-created_at',)
