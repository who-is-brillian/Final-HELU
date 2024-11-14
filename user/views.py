from django.shortcuts import render
from user.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # Hash the password
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(
        request,
        "signup.html",
        {
            "user_form": user_form,
            "registered": registered,
        },
    )

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")  # Get from login.html
        password = request.POST.get("password")  # Get from login.html

        user = authenticate(email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print(f"email: {email} and password: {password}")
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, "login.html", {})