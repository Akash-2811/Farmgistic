from django.urls import path

from . import views

urlpatterns = [
    path('traders/', views.traders, name="traders"),
    path('trader_profile/<int:id>', views.trader_profile, name="trader_profile"),
    path('search_crop/<str:name>', views.search_crop, name="search_crop"),
    path('crop_detail/<int:id>/', views.crop_detail, name="crop_detail"),
    path('orders/<int:id>/', views.order, name="orders"),
    path('address/<int:id>', views.address, name="address"),
    path('logout/', views.logout_user, name="logout"),
]