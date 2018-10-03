from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from vaultApp.models import PasswordEntry
from .forms import LoginForm, SignupForm

# Create your views here.
def index(request):
    template_name = "app/index.html"
    entryList = PasswordEntry.objects.filter(created=True)

    return render(request, template_name, {"entryList" : entryList})

def register(request):
    template_name = "registration/register.html"

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password")
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignupForm()

    return render(request, template_name, {"form": form})

def user_login(request):
    template_name = "registration/login.html"

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
            else:
                return render(request, template_name, {"error" : "Incorrect username/password or both."})
    else:
        form = LoginForm()

    return render(request, template_name, {'form': form})

@login_required
def user_logout(request):
    template_name = "app/index.html"
    logout(request)

    return render(request, template_name)