from django import forms
from .models import Wear,GENDER_CHOICES
class WearForm(forms.Form):
    name  = forms.CharField(label = 'Nombre del atuendo')
    img = forms.ImageField(label = 'Seleciona una Modelo')
    desc = forms.CharField(label = 'Descripcion',
	widget = forms.Textarea(
			attrs = {
			'placeholder': 'Escriba una descripcion detallada, por favor',
			'id': 'nombreID',
			'class': 'special',
			'cols': '66',
			'rows': '3',
			}

		)
	)
    quant = forms.IntegerField(label = 'Cantidad', initial = 100)
    price = forms.IntegerField(label = 'Precio', initial = 100)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    offer = forms.BooleanField(label = 'Promociòn', required = False, initial = None)
