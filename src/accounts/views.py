from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from .models import User
from .forms import UserForm
from .models import Profile
from shoping_cart.models import Order

# Create your views here.

def register(request):    
    if request.method == 'POST':        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']      
        phone = request.POST['phone']
        direction = request.POST['direction']          	
        password = request.POST['password']
        password2 = request.POST['password2']		
        User=get_user_model()
        if password==password2:			
            if User.objects.filter(email=email).exists():
                messages.info(request,'Este email ya existe')
                return redirect('registro')
            else:
                                
                user= User.objects.create_user(password=password, email=email, first_name=first_name, last_name=last_name, phone=phone, direction=direction)
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

def logout(request):
	auth.logout(request)
	return redirect('/')

def regreso(request):
	return redirect('/')

def profile(request):
	user_profile = Profile.objects.filter(user=request.user).first()
	user_orders = Order.objects.filter(is_ordered=True, owner=user_profile)
	context = {
		'user_orders': user_orders
	}

	return render(request, "profile.html", context)