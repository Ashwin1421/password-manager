from django.shortcuts import render
from vaultApp.models import PasswordEntry

# Create your views here.
def index(request):
    template_name = "passwordentry/index.html"
    entryList = PasswordEntry.objects.filter(created=True)

    return render(request, template_name, {"entryList" : entryList})