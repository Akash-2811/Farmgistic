from django.urls import path

from . import views

urlpatterns = [
    path('login_farmer/', views.login_farmer, name="login_farmer"),
    path('login_trader/', views.login_trader, name="login_trader"),
    path('farmer_register/', views.farmer_register, name="farmer_register"),
    path('trader_register/', views.trader_register, name="trader_register"),
    path('logout/', views.logout_user, name="logout")
]