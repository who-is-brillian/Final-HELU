from django.shortcuts import render, redirect
from user.forms import UserForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Halaman index
def index(request):
    return render(request, "index.html")

# Halaman khusus untuk user yang sudah login
@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

# View untuk logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# View untuk registrasi
def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)  # Meng-hash password
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

# View untuk login
def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")  # Ambil dari form login.html
        password = request.POST.get("password")  # Ambil dari form login.html

        user = authenticate(request, email=email, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)  # Gunakan auth_login dari django
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print(f"email: {email} and password: {password}")
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, "login.html", {})
