from django.urls import path
from django.contrib.auth.views import auth_logout
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "vaultApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("entry/", views.index, name="entry"),
]