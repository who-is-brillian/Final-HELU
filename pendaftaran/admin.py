from django.contrib import admin
from pendaftaran.models import Pendaftaran

# Register your models here.

admin.site.register(Pendaftaran)

# @admin.register(Pendaftaran)
# class PendaftaranAdmin(admin.ModelAdmin):
#     list_display = ('nama', 'status_pembayaran', 'kelas', 'level')
#     actions = ['set_status_lunas']

#     def set_status_lunas(self, request, queryset):
#         queryset.update(status_pembayaran='lunas')
#         self.message_user(request, "Status pembayaran berhasil diperbarui ke 'Lunas'.")
#     set_status_lunas.short_description = "Set status to 'Lunas'"
