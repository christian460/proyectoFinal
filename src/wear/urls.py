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
	path('category/',views.category,name="category"),
	path('category/mens',views.categoryMens,name="category"),
	path('category/womens',views.categoryWomens,name="category"),
	path('category/singleProduct/<int:myID>/',views.singleProduct,name="category"),
]