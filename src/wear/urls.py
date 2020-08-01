from django.urls import path, include

from . import views
urlpatterns=[
	path("", views.index, name="index"),
	path("index", views.regreso, name="index"),
	path("login", views.login, name="login"),
	path("regisropa", views.regisropa, name="regisropa"),
	path("contactar", views.contactar, name="contactar"),
	path('cliente/', include('cliente.urls')),
	path('ropa',views.createWear,name="nada"),
]