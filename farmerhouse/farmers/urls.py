from django.urls import path

from . import views

urlpatterns = [
    path('farmers/', views.farmers, name="farmers"),
    path('farmer_profile/<int:id>/', views.farmer_profile, name="farmer_profile"),
    path('add_crop/', views.add_crop, name="add_crop"),
    path('search_crop/<str:name>', views.search_crop, name="search_crop"),
    path('orders/<int:id>/', views.orderfr, name="orderfr"),
    path('logout/', views.logout_user, name="logout"),

]