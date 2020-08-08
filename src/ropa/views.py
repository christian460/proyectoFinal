from django.conf import settings
from django.shortcuts import render,redirect
from .models import Ropa
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
# Create your views here.

def index(request):
	rops=Ropa.objects.all()
	return render(request,"index.html", {'rops':rops})

def regreso(request):
	return redirect('/')

def login(request):
	return render(request,"login.html")

def rop_hom(request):
	rops=Ropa.objects.all()
	return render(request,'rop_hom.html',{'rops':rops})

def rop_muj(request):
	rops=Ropa.objects.all()
	return render(request,'rop_muj.html',{'rops':rops})

def rop_tod(request):
	rops=Ropa.objects.all()
	return render(request,'rop_tod.html',{'rops':rops})

def regisropa(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		modelo = request.FILES['modelo']
		des = request.POST['des']
		cat = request.POST['cat']
		pre=request.POST['pre']
		prom=request.POST['prom']
		rops=Ropa.objects.all()
		for rop in rops:
			if rop.nombre==nombre and rop.modelo==modelo:
				messages.info(request,'Esta prenda ya existe')
				return redirect('regisropa')
			ropa=Ropa.objects.create(nombre=nombre, modelo=modelo, des=des, cat=cat, pre=pre, prom=prom)
			ropa.save();
			return redirect('/')
	else:
		return render(request,'registro_ropa.html')

def modificar(request):
	rops=Ropa.objects.all()
	if request.method == 'POST':
		nombre = request.POST['nombre']
		modelo = request.FILES['modelo']
		des = request.POST['des']
		cat = request.POST['cat']
		pre=request.POST['pre']
		prom=request.POST['prom']
		for rop in rops:
			if rop.nombre!=nombre:
				messages.info(request,'Esta prenda no existe')
				return redirect('regisropa')
			else:
				rop.modelo=modelo
				rop.des=des
				rop.cat=cat
				rop.pre=pre
				rop.prom=prom
				rop.save();
				return redirect('/')
	else:
		return render(request,'modificar_rop.html',{'rops':rops})

def contactar(request):
	return render(request,"contact.html")

def correo_prom(request):
	if request.method == 'POST':
		asunto=request.POST['asunto']
		mensaje=request.POST['mensaje']
		correo=request.POST['correo']
		envio_prom(asunto,mensaje,correo)
		return redirect('/')
	else:
		return render(request,'correo_prom.html')

def envio_prom(asunto,mensaje,correo):
	context={'asunto':asunto,'mensaje':mensaje}
	template= get_template('prom.html')
	content= template.render(context)
	email= EmailMultiAlternatives(
		'Un correo',
		'django',
		settings.EMAIL_HOST_USER,
		[correo]
	)
	email.attach_alternative(content,'text/html')
	email.send()
