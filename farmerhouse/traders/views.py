from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from webpages.models import crop_details
from authentication.models import trader_auth, farmer_auth
from farmers.models import crops, images
from traders.models import orders
#from .models import trader_auth

# Create your views here.
def traders(request):
    crops = crop_details.objects.all()
    profile = request.session['email']
    print(profile)
    trader = trader_auth.objects.get(email=profile)
    
    data= {
        'crops': crops,
        'trader': trader,
    }

    return render(request, 'traders/traders.html',data)


def trader_profile(request, id):
    trader = trader_auth.objects.get(id=id)

    data = {
        'trader': trader,
    }
    return render(request, 'traders/trader_profile.html', data)

def search_crop(request, name):
    print(name)
    crop = crops.objects.filter(crop_name=name)
    data={
        'crop': crop
    }
    return render(request, 'traders/search_crop.html', data)

def crop_detail(request, id):
    crop = crops.objects.filter(id=id)
    data = {
        'crop': crop
    }
    return render(request, 'traders/crop_detail.html', data)

def order(request, id):
    
    trader = request.session['id']
    crop = crops.objects.last()
    packet = orders(crops_id=crop, trader_id=trader)
    packet.save()
    packets = orders.objects.filter(trader_id=trader)
    
    
    data = {
        'packets': packets,
        'crop': crop,
    }
    
    return render(request, 'traders/orders.html',data)

def address(request, id):
    trader = trader_auth.objects.get(id=id)

    data = {
        'trader': trader,
    }
    return render(request, 'traders/address.html', data)

def logout_user(request):
    logout(request)
    messages.success(request, 'you are logged out')
    return redirect('index')