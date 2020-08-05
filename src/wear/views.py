from django.shortcuts import render,redirect
from .models import Wear
from django.contrib import messages
from .forms import WearForm
# Create your views here.

def index(request):
	return render(request,"index.html")

def regreso(request):
	return redirect('/')

def login(request):
	return render(request,"login.html")

def regisropa(request):
	form = WearForm()			
	if request.method == 'POST':
		form = WearForm(request.POST, request.FILES)
		if form.is_valid():
			print(form.cleaned_data)
			Wear.objects.create(**form.cleaned_data)
			return redirect ("/")
		else:
			print(form.errors)

	context = {
		'form':form
	}

	return render(request,'registro_ropa.html',context)

def createWear(request):
	form = WearForm()			
	if request.method == 'POST':
		form = WearForm(request.POST, request.FILES)
		if form.is_valid():
			print(form.cleaned_data)
			Wear.objects.create(**form.cleaned_data)
		else:
			print(form.errors)

	context = {
		'form':form
	}
	return render(request,'registro_ropa.html',context)

def contactar(request):
	return render(request,"contact.html")