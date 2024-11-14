from django.shortcuts import render
from django.contrib import messages
from .forms import MailboxForm
from django.templatetags.static import static

def contact(request):
    # Untuk menangani form kontak dan juga menambahkan data banner
    context = {
        'title': 'Contact Us - HELU',  # Judul untuk halaman
        'bannerClass': static('images/AboutUs.png'),  # Static image untuk banner
    }

    # Jika form disubmit
    if request.method == 'POST':
        form = MailboxForm(request.POST)

        if form.is_valid():
            # Menampilkan data form yang dikirimkan di konsol (debugging)
            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data["mail_name"])
            print("EMAIL: " + form.cleaned_data["mail_email"])
            print("TEXT: " + form.cleaned_data["mail_message"])

            # Menyimpan form
            form.save()

            # Reset form setelah berhasil
            form = MailboxForm()

            # Menambahkan pesan sukses ke notifikasi
            messages.success(request, "Your message has been sent successfully!")

    else:
        # Jika tidak ada data POST, buat instance form kosong
        form = MailboxForm()

    # Menambahkan form ke context
    context['form'] = form

    # Render halaman contact.html dengan context yang sudah disiapkan
    return render(request, 'contact.html', context)
