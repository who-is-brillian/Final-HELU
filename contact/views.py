from django.shortcuts import render
from django import forms
from .forms import MailboxForm
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = MailboxForm(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data["mail_name"])
            print("EMAIL: " + form.cleaned_data["mail_email"])
            print("TEXT: " + form.cleaned_data["mail_message"])
            form.save()
            form = MailboxForm()
            messages.success(request, "VALIDATION SUCCESS!")

    else:
        form = MailboxForm()

    return render(request, 'contact.html', context={'form':form})
