from django.urls import path , include
from . import views

urlpatterns = [
    path('ask/', views.ask, name = 'ask'),
    path('',views.home, name = 'home'),
    path('register/', views.registerpage, name = 'register'),
    path('login/', views.loginpage, name = 'login')
]