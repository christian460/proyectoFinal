from django.db import models

# Create your models here.
class Ropa(models.Model):
	nombre=models.CharField(max_length=100)
	modelo=models.ImageField(upload_to='pics')
	des=models.TextField()
	cat=models.CharField(max_length=100)
	pre=models.IntegerField()
	prom=models.BooleanField()

