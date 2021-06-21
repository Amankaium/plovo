from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Email


def main(request):
    return render(request, 'index.html')


def success(request):
    subject = request.POST.get('subject')
    email = request.POST.get('email')
    data = request.POST.get('text')
    
    Email(subject=subject, email_to=email, text=data).save()

    return render(request, 'success.html')
