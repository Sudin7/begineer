from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, ConsultationForm
from .models import NewsItem, DownloadableFile, FAQItem, ConsultationRequest


def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject'] or 'New inquiry from website'
        message = form.cleaned_data['message']

        email_subject = f"{subject} - {name}"
        email_message = f"Name: {name}\nEmail: {email}\n\n{message}"

        send_mail(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully.')
        return redirect('contact')

    return render(request, 'contact.html', {'form': form})


def news_view(request):
    news_list = NewsItem.objects.filter(is_published=True)
    return render(request, 'news.html', {'news_list': news_list})


def downloads_view(request):
    files = DownloadableFile.objects.all()
    return render(request, 'downloads.html', {'files': files})


def faq_view(request):
    faqs = FAQItem.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})


def consultation_view(request):
    form = ConsultationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        consultation = ConsultationRequest.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            preferred_date=form.cleaned_data['preferred_date'],
            preferred_time=form.cleaned_data['preferred_time'],
            message=form.cleaned_data['message'],
        )

        send_mail(
            f"Consultation request from {consultation.name}",
            f"Name: {consultation.name}\nEmail: {consultation.email}\nPhone: {consultation.phone}\nDate: {consultation.preferred_date or 'Any'}\nTime: {consultation.preferred_time or 'Any'}\n\nMessage:\n{consultation.message}",
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_RECIPIENT_EMAIL],
            fail_silently=False,
        )
        messages.success(request, 'Your consultation request has been received. We will contact you soon.')
        return redirect('consultation')

    return render(request, 'consultation.html', {'form': form})
