from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class Cliente(AbstractUser):
	telefono=models.IntegerField(default=0)
	direccion=models.CharField(max_length=100, default=' ')
	sexo=models.CharField(max_length=100, default=' ')
		