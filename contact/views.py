from django.shortcuts import render
from django import forms
from .forms import MailboxForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = MailboxForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = MailboxForm()

    return render(request, 'contact.html', context={'form':form})
