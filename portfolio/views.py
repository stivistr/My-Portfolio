from django.shortcuts import render
from .models import Project
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct email message
            subject = f'New Contact Form Submission from {name}'
            full_message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'

            # Send email
            send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['stivistr@gmail.com'])

            return render(request, 'portfolio/contact.html', {'form': form, 'success': True})

    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})