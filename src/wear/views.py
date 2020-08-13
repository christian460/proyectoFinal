from __future__ import unicode_literals
from django.shortcuts import render,redirect, get_object_or_404
from .models import Wear
from django.contrib import messages
from .forms import WearForm, WearForm2
from accounts.models import User, Profile
from shoping_cart.models import Order


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

def editWear(request,myID):
	wear = get_object_or_404(Wear,id = myID)		
	form = WearForm2(request.POST or None, instance = wear)	
	if form.is_valid():
		form.save()
		form = WearForm()
		return redirect ('/')

	context = {
		'form':form
	}

	return render(request, 'edit_ropa.html', context)

def deleteWear(request, myID):
	obj = get_object_or_404(Wear,id = myID)
	if request.method == 'POST':
		print("Borrado")
		obj.delete()
		return redirect('/')			
	context = {
		'objeto' : obj,
	}		
	return render(request,'delete_ropa.html',context)

def listWear(request):
	queryset = Wear.objects.all()
	context ={
		'objectList': queryset
	}
	return render(request, 'listWear.html',context)

def category(request):
	wears = Wear.objects.all()
	filtered_orders = Order.objects.filter(owner = request.user.profile, is_ordered=False)
	current_order_wears = []
	
	if filtered_orders.exists():
		user_order = filtered_orders[0]
		user_order_items = user_order.items.all()
		current_order_wears = [product.product for product in user_order_items]
	context = {
		'wears':wears,
		'current_order_wears':current_order_wears
	}
	return render(request,"category.html",context)

def categoryMens(request):
	wears = Wear.objects.all()
	filtered_orders = Order.objects.filter(owner = request.user.profile, is_ordered=False)
	current_order_wears = []
	
	if filtered_orders.exists():
		user_order = filtered_orders[0]
		user_order_items = user_order.items.all()
		current_order_wears = [product.product for product in user_order_items]
	context = {
		'wears':wears,
		'current_order_wears':current_order_wears
	}
	return render(request,"categoryMens.html",context)

def categoryWomens(request):
	wears = Wear.objects.all()
	filtered_orders = Order.objects.filter(owner = request.user.profile, is_ordered=False)
	current_order_wears = []

	if filtered_orders.exists():
		user_order = filtered_orders[0]
		user_order_items = user_order.items.all()
		current_order_wears = [product.product for product in user_order_items]
	context = {
		'wears':wears,
		'current_order_wears':current_order_wears
	}
	return render(request,"categoryWomens.html",context)

def singleProduct(request,myID):
	wear = get_object_or_404(Wear,id = myID)
	filtered_orders = Order.objects.filter(owner = request.user.profile, is_ordered=False)
	current_order_wears = []
	
	if filtered_orders.exists():
		user_order = filtered_orders[0]
		user_order_items = user_order.items.all()
		current_order_wears = [product.product for product in user_order_items]
	context ={
		'wear':wear,
		'current_order_wears':current_order_wears
	}
	return render(request, 'singleProduct.html',context)
