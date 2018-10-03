from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()



class PasswordEntry(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    plaintext_password = models.CharField(max_length=150)
    password_hash = models.CharField(max_length=512)
    created = models.BooleanField(default=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        result = "Entry{"
        result += "Id="+str(self.id)+", "
        result += "userName=" + str(self.username) + ", "
        result += "password="+str(self.plaintext_password)
        result += " }"
        return result


