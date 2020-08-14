from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('my_profile/', views.profile,name='profile'),
    path("correo_prom/", views.correo_prom, name="correo_prom"),
]