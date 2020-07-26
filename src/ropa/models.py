from django.db import models

# Create your models here.
class Ropa(models.Model):
	nombre=models.CharField(max_length=100)
	modelo=models.ImageField(upload_to='pics')
	color=models.CharField(max_length=100)
	material=models.CharField(max_length=100)
	talla=models.CharField(max_length=5)
	pre=models.IntegerField()
	prom=models.BooleanField()
