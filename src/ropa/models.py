from django.db import models

# Create your models here.
class Wear(models.Model):
	name = models.CharField(max_length=100)
	modelo=models.ImageField(upload_to='pics')
	des=models.TextField()
	cant=models.CharField(max_length=100)
	pre=models.IntegerField()
	prom=models.BooleanField()

