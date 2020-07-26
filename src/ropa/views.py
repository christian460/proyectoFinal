from django.shortcuts import render,redirect
from .models import Ropa
from django.contrib import messages
# Create your views here.

def index(request):
	return render(request,"index.html")

def regreso(request):
	return redirect('/')

def login(request):
	return render(request,"login.html")

def regisropa(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		modelo = request.POST['modelo']
		color = request.POST['color']
		material = request.POST['material']
		talla = request.POST['talla']
		pre=request.POST['pre']
		prom=request.POST['prom']
		rops=Ropa.objects.all()
		for rop in rops:
			if rop.nombre!=nombre and rop.modelo!=modelo:
				messages.info(request,'Esta prenda ya existe')
				return redirect('regisropa')
			ropa=Ropa.objects.create(nombre=nombre, modelo=modelo, color=color, material=material, talla=talla, pre=pre, prom=prom)
			ropa.save();
			return redirect('/')
	else:
		return render(request,'registro_ropa.html')

def contactar(request):
	return render(request,"contact.html")