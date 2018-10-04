from django.urls import path
from django.contrib.auth.views import auth_logout
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "vaultApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/profile/", views.index, name="profile"),
    path("new/", views.create_password_entry, name="new_entry"),
    path("delete/<int:pk>/", views.delete_password_entry, name="delete_entry"),
    path("sign-in/", views.user_login, name="login"),
    path("sign-up/", views.register, name="register"),
    path("sign-out/", views.user_logout, name="logout"),
]