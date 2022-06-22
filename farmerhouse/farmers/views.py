from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import farmer_auth
from webpages.models import crop_details
from farmers.models import crops, images
from authentication.models import farmer_auth, trader_auth
from traders.models import orders

# Create your views here.

def farmers(request):

    crops = crop_details.objects.all()
    profile = request.session['email']
    
    farmer = farmer_auth.objects.get(email=profile)
    data= {
        'crops': crops,
        'farmer': farmer,
    }

    return render(request, 'farmers/farmers.html', data)

def farmer_profile(request, id):
    farmer = farmer_auth.objects.get(id=id)

    data = {
        'farmer': farmer,
    }
    return render(request, 'farmers/farmer_profile.html', data)

def add_crop(request):

    email = request.session['email']
    user = farmer_auth.objects.all()
    for u in user:
        if email == u.email:
            u_id = u.id
            

    farmer = farmer_auth.objects.filter(id=u_id)
    if request.method == 'POST':
        crop_name = request.POST['crop_name']
        print(crop_name)
        crop_price = request.POST['crop_price']
        quantity = request.POST['crop_quantity']
        imgs = request.POST['url']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = farmer_auth.objects.get(email=email)
        
        print(user)
        if password == user.password:
            if confirm_password == password:
                crop = crops(farmer_id=user, crop_name=crop_name, quantity=quantity, price=crop_price, image_link=imgs)

                crop.save()

        return redirect('farmers')

    return render(request, 'farmers/add_crop.html')


def search_crop(request, name):
    print(name)
    crop = crops.objects.filter(crop_name=name)
    data={
        'crop': crop
    }
    return render(request, 'traders/search_crop.html', data)



def orderfr(request, id):
    farmer = farmer_auth.objects.get(id=id)
    crop = crops.objects.filter(farmer_id=id)
    
    data = {
        'farmer': farmer,
        'crop': crop,
    }
    return render(request, 'farmers/orders.html', data)


def logout_user(request):
    logout(request)
    messages.success(request, 'you are logged out')
    return redirect('index')