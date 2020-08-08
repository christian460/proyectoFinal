from django.urls import path, include

from . import views
urlpatterns=[
	path("", views.index, name="index"),
	path("index", views.regreso, name="index"),
	path("login", views.login, name="login"),
	path("regisropa", views.regisropa, name="regisropa"),
	path("contactar", views.contactar, name="contactar"),
	path('correo_prom', views.correo_prom, name="correo_prom"),
	path('cliente/', include('cliente.urls')),
	path("rop_hom", views.rop_hom, name="rop_hom"),
	path("rop_muj", views.rop_muj, name="rop_muj"),
	path("rop_tod", views.rop_tod, name="rop_tod"),
	path("modificar", views.modificar, name="modificar"),
]
