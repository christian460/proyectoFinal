from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, auth
# Create your views here.

def registro(request):
	if request.method == 'POST':
		nombre = request.POST['first_name']
		apellidos = request.POST['last_name']
		email = request.POST['email']
		usuario = request.POST['username']
		contraseña1 = request.POST['password1']
		contraseña2 = request.POST['password2']
		telefono = request.POST['telefono']
		direccion = request.POST['direccion']
		User=get_user_model()
		if contraseña1==contraseña2:
			if User.objects.filter(username=usuario).exists():
				messages.info(request,'Este usuario ya existe')
				return redirect('registro')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Este email ya existe')
				return redirect('registro')
			else: 	
				user= User.objects.create_user(username=usuario, password=contraseña1, email=email, first_name=nombre, last_name=apellidos, telefono=telefono, direccion=direccion)
				user.save();
				print ('Usuario creado')
				return redirect('/')
		else:
			messages.info(request, 'Las contraseñas no coinciden')
			return redirect('register')
		return redirect('/')
	else:
		return render(request,'registro.html')

def login(request):
	if request.method == 'POST':
		print('lol')
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			print('Inicio secion')
			return redirect("/")
		else:
			messages.info(request,'Datos erroneos')
			return redirect('login')
	else:
		return render(request,'login.html')

def cerrarSesion(request):
	auth.logout(request)
	return redirect('/')

def regreso(request):
	return redirect('/')


