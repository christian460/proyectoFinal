from django.db import models

# Create your models here.
GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

class Wear(models.Model):
	name = models.CharField(max_length=100)
	img = models.ImageField(upload_to='pics')
	desc = models.TextField()
	quant = models.CharField(max_length=100)
	price = models.IntegerField()
	gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
	offer = models.BooleanField()

	def __unicode__(self):
		return str(self.img)   



