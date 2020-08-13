from django import forms
from .models import Wear,GENDER_CHOICES

class WearForm2(forms.ModelForm):
	class Meta:
		model = Wear		
		fields =[
			'name',
			'img',
			'desc',
			'quant',
			'price',
			'gender',
			'offer'
		]
		widgets ={
			'gender':forms.RadioSelect(),
			'desc':forms.Textarea(
				attrs = {				
				'id': 'nombreID',
				'class': 'special',
				'cols': '40',
				'rows': '2',
			})
		}
	
class WearForm(forms.Form):
	name  = forms.CharField(label = 'Nombre del atuendo')
	img = forms.ImageField(label = 'Seleciona una Modelo')
	desc = forms.CharField(label = 'Descripcion',
	widget = forms.Textarea(
			attrs = {
			'placeholder': 'Escriba una descripcion detallada, por favor',
			'id': 'nombreID',
			'class': 'special',
			'cols': '40',
			'rows': '2',
			}
		)
	)
	quant = forms.IntegerField(label = 'Cantidad', initial = None)
	price = forms.IntegerField(label = 'Precio', initial = None)
	gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
	offer = forms.BooleanField(label = 'Promociòn', required = False, initial = None)
