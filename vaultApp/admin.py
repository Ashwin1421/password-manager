from django.contrib import admin
from vaultApp.models import PasswordEntry

# Register your models here.
class PasswordEntryAdmin(admin.ModelAdmin):
    list_display = ['id','user_name','plaintext_password']
    search_fields = ['username']
    save_on_top = True


admin.site.register(PasswordEntry, PasswordEntryAdmin)