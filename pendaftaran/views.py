from django.shortcuts import render, redirect
from .forms import PendaftaranForm
from .models import Pendaftaran
from django.contrib.auth.decorators import login_required

@login_required  # Pastikan pengguna harus login
def base_view(request):
    print("Base view is called")  # Debug: Cek apakah view ini dipanggil
    user_pendaftaran = Pendaftaran.objects.filter(user=request.user, status_pembayaran='Lunas').exists()

    # Debug: Cek nilai yang dikirim ke template
    print(f"Authenticated user: {request.user.username}, show_nav_button: {user_pendaftaran}")

    return render(request, 'base.html', {'show_nav_button': user_pendaftaran})


# def base_view(request):
#     user_pendaftaran = Pendaftaran.objects.filter(user=request.user, status_pembayaran='Lunas').exists()
#     return render(request, 'base.html', {'show_nav_button': user_pendaftaran})

def target_view(request):
    # Logika tampilan untuk pengguna dengan status "Lunas"
    return render(request, 'target.html')

@login_required
def pendaftaran_view(request):
    if request.method == 'POST':
        form = PendaftaranForm(request.POST, request.FILES)
        if form.is_valid():
            pendaftaran = form.save(commit=False)
            pendaftaran.user = request.user
            pendaftaran.email = request.user.email

            # Logika harga berdasarkan kelas dan level
            harga_dict = {
                'Kelas Grammar': {'Beginner': 200000, 'Intermediate': 250000, 'Advanced': 300000},
                'Kelas Listening': {'Beginner': 250000, 'Intermediate': 300000, 'Advanced': 350000},
                'Kelas Reading': {'Beginner': 180000, 'Intermediate': 220000, 'Advanced': 280000},
                'Kelas Writing': {'Beginner': 230000, 'Intermediate': 270000, 'Advanced': 320000},
                'Kelas Speaking': {'Beginner': 240000, 'Intermediate': 290000, 'Advanced': 340000},
                'Toefl Preparation': {'Beginner': 300000, 'Intermediate': 350000, 'Advanced': 400000},
                'Ielts Preparation': {'Beginner': 320000, 'Intermediate': 370000, 'Advanced': 420000},
                'Business English': {'Beginner': 350000, 'Intermediate': 400000, 'Advanced': 450000},
            }

            # Pastikan kelas dan level ada dalam harga_dict
            if pendaftaran.kelas in harga_dict and pendaftaran.level in harga_dict[pendaftaran.kelas]:
                pendaftaran.harga = harga_dict[pendaftaran.kelas][pendaftaran.level]
                pendaftaran.save()
                return redirect('pembayaran_sukses')  # Mengarahkan ke halaman sukses
            else:
                # Jika kelas atau level tidak valid, bisa menampilkan error atau pesan
                form.add_error(None, "Kelas atau level tidak valid.")
    else:
        form = PendaftaranForm()

    return render(request, 'pendaftaran/pembayaran_form.html', {'form': form})

# View untuk menampilkan halaman sukses setelah pembayaran
@login_required
def pembayaran_sukses_view(request):
    return render(request, 'pendaftaran/pembayaran_sukses.html')
