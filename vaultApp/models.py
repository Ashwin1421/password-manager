from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class PasswordEntry(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=150)
    plaintext_password = models.CharField(max_length=150)
    password_hash = models.CharField(max_length=512)
    created = models.BooleanField(default=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        result = "Entry{"
        result += "Id="+str(self.id)+", "
        result += "userName=" + str(self.user_name) + ", "
        result += "password="+str(self.plaintext_password)
        result += " }"
        return result


