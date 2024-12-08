# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

@login_required
def user_profile(request):
    # Mengambil data user yang sedang login
    user = request.user
    if request.method == 'POST':
        # Jika ada POST, kita perbarui data pengguna
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect kembali ke halaman profil
    else:
        # Jika GET, tampilkan data pengguna yang sudah ada
        form = UserProfileForm(instance=user)

    return render(request, 'user_profile/profile.html', {'form': form})

@login_required
def edit_profile(request):
    user = request.user  # Mengambil data user yang sedang login
    return render(request, 'user_profile/user_profile.html', {'user': user})

