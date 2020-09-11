from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('register/register', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('login/login', views.login, name="login"),
    path('login/logout/', views.logout, name="logout"),
    path('veg.html', views.veg, name="veg"),
    path('nonveg.html', views.nonveg, name="nonveg"),
    path('vegan.html', views.vegan, name="vegan"),
]