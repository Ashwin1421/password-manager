from django.db import models

# Create your models here.
class PasswordEntry(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=150)
    plainTextPassword = models.CharField(max_length=150)
    passwordHash = models.CharField(max_length=512)
    created = models.BooleanField(default=True)
    dateOfCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        result = "Entry{"
        result += "Id="+str(self.id)+", "
        result += "userName="+str(self.userName)+", "
        result += "password="+str(self.plainTextPassword)
        result += " }"
        return result

