from django.db import models

# Create your models here.


class UserLogin(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"Email: {self.email}, Password: {self.password}"

