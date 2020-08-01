from django import forms
from .models import User, GENERO,YES_NO


class UserForm(forms.Form):

    email = forms.EmailField(label="Correo Electronico",max_length= 100,required=True)
    first_name = forms.CharField(label="Nombres",max_length=100,required=True)    
    last_name = forms.CharField(label="Apellidos",max_length=100,required=True)
    phone = forms.IntegerField(label="Numero Telefonico")
    direction =forms.CharField(label="Direcciòn",max_length=100,required=True)
    gender = forms.ChoiceField(choices=GENERO, widget=forms.RadioSelect())
    active = forms.BooleanField()
    staff = forms.BooleanField()
    admin = forms.BooleanField()