from django.urls import path, include
from . import views

urlpatterns=[
	path("registro", views.registro, name="registro"),
	path("logout", views.cerrarSesion, name="cerrarSesion"),
	path("login", views.login, name="login"),
	path("regreso", views.regreso, name="regreso"),
	path("correo_prom", views.correo_prom, name="correo_prom"),
]