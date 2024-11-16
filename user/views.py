from django.shortcuts import render, redirect
from user.forms import UserForm, UserProfileInfoForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.backends import ModelBackend


# index page
def index(request):
    return render(request, "index.html")

# Page when user is logged in
@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

# Logout user
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("home:index"))

@csrf_protect
def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # Hash the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user  # OneToOne relationship

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(
        request,
        "register.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "registered": registered,
        },
    )

# Login page
def user_login(request):
    error_message = None  # Inisialisasi variabel error_message

    if request.method == "POST":
        email = request.POST.get("email")  # Ambil email dari form
        password = request.POST.get("password")  # Ambil password dari form

        user = authenticate(request, username=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("home:index"))
            else:
                error_message = "Account is not active."
        else:
            error_message = "Invalid login details. Please try again."
    
    # Kirim pesan error (jika ada) ke template
    return render(request, "login.html", {"error_message": error_message})


