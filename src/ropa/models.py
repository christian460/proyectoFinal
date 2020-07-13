from django.db import models

# Create your models here.
class Ropa(models.Model):
	nombre=models.CharField(max_length=100)
	modelo=models.CharField(max_length=100)
	color=models.CharField(max_length=100)
	material=models.CharField(max_length=100)
	talla=models.CharField(max_length=5)
	pre=models.IntegerField()
