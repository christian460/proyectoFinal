from django.shortcuts import render,redirect
from .models import Ropa
from django.contrib import messages
# Create your views here.

def index(request):
	rops=Ropa.objects.all()
	return render(request,"index.html", {'rops':rops})

def regreso(request):
	return redirect('/')

def login(request):
	return render(request,"login.html")

def regisropa(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		modelo = request.POST['modelo']
		des = request.POST['des']
		cat = request.POST['cat']
		pre=request.POST['pre']
		prom=request.POST['prom']
		rops=Ropa.objects.all()
		for rop in rops:
			if rop.nombre!=nombre and rop.modelo!=modelo:
				messages.info(request,'Esta prenda ya existe')
				return redirect('regisropa')
			ropa=Ropa.objects.create(nombre=nombre, modelo=modelo, des=des, cat=cat, pre=pre, prom=prom)
			ropa.save();
			return redirect('/')
	else:
		return render(request,'registro_ropa.html')

def contactar(request):
	return render(request,"contact.html")