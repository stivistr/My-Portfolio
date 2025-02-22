from django.shortcuts import render
from .models import Project
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # For now, we'll just print the data to the console.
            print(form.cleaned_data)
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})