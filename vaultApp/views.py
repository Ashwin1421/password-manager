from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from vaultApp.models import PasswordEntry
from .forms import LoginForm, SignupForm, PasswordEntryForm, RandomPasswordGenerationForm
from email_validator import validate_email, EmailNotValidError, EmailUndeliverableError, EmailSyntaxError
from .security.policy import Policy
from .security.hashing import PasswordHashing
from .security.manager import PasswordGenerator


# Create your views here.
def index(request):
    template_name = "app/index.html"
    if request.user.is_authenticated:
        entry_list = PasswordEntry.objects.filter(created=True, account=request.user)
    else:
        entry_list = []

    return render(request, template_name, {"entry_list": entry_list})


def register(request):
    template_name = "registration/register.html"

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            try:
                v = validate_email(email, check_deliverability=True)
                email = v["email"]
            except EmailUndeliverableError as e:
                print(str(e))
            except EmailNotValidError as e:
                print(str(e))
            except EmailSyntaxError as e:
                print(str(e))
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
                return render(request, template_name, {"error": "Incorrect username/password or both."})
    else:
        form = LoginForm()

    return render(request, template_name, {'form': form})


@login_required
def user_logout(request):
    logout(request)

    return redirect("/")


@login_required
def create_password_entry(request):
    template_name = "app/password_entry_form.html"
    password_hashing = PasswordHashing(algorithm="sha512")

    if request.method == "POST":
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            new_password_entry = PasswordEntry()
            new_password_entry.username = form.cleaned_data.get("username")
            new_password_entry.plaintext_password = form.cleaned_data.get("plaintext_password")
            new_password_entry.created = True
            password_hash = password_hashing.get_hash_value(new_password_entry.plaintext_password)
            new_password_entry.password_hash = password_hash
            if request.user.is_authenticated:
                new_password_entry.account = request.user

            new_password_entry.save()

            return redirect("/")
    else:
        form = PasswordEntryForm()

    return render(request, template_name, {"form": form})


@login_required
def update_password_entry(request, pk):
    template_name = "app/password_entry_form.html"
    entry = get_object_or_404(PasswordEntry, pk=pk)

    if request.method == "POST":
        form = PasswordEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()

            return redirect("/")
    else:
        form = PasswordEntryForm(None, instance=entry)

    return render(request, template_name, {"form": form})


@login_required
def delete_password_entry(request, pk):
    # make a separate template for delete action
    template_name = "app/index.html"
    password_entry = get_object_or_404(PasswordEntry, pk=pk)
    if request.method == "POST":
        password_entry.delete()

        return redirect("/")

    return render(request, template_name, {"password_entry": password_entry})


@login_required
def detail_password_entry(request, pk):
    template_name = "app/password_entry_detail.html"
    password_entry = get_object_or_404(PasswordEntry, pk=pk)

    if request.user.is_authenticated:
        entry_list = PasswordEntry.objects.filter(created=True)
    else:
        entry_list = []

    return render(request, template_name, { "entry_list": entry_list, "entry": password_entry})


@login_required
def gen_rnd_password(request, pk):
    template_name = "app/password_entry_detail.html"
    password_entry = get_object_or_404(PasswordEntry, pk=pk)
    policy = Policy(
        length=16,
        has_lowercase=True,
        has_uppercase=True,
        has_numbers=True,
        has_special_chars=True
    )
    manager = PasswordGenerator(policy)
    context = dict()
    if request.method == "POST":
        random_password = manager.get_random_password()

        if request.user.is_authenticated:
            entry_list = PasswordEntry.objects.filter(created=True, account=request.user)
        else:
            entry_list = []
        context["entry_list"] = entry_list
        context["entry"] = password_entry
        context["random_password"] = random_password
        print(random_password)

        return render(request, template_name, context)