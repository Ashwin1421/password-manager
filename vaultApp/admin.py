from django.contrib import admin
from vaultApp.models import PasswordEntry

# Register your models here.
class PasswordEntryAdmin(admin.ModelAdmin):
    list_display = ['id','userName','plainTextPassword']
    search_fields = ['userName']
    save_on_top = True


admin.site.register(PasswordEntry, PasswordEntryAdmin)