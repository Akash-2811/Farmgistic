from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import farmer_auth, trader_auth
from django.contrib.auth.decorators import login_required

import os


# Create your views here.




global u_id

def login_farmer(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = farmer_auth.objects.filter(email__iexact=email)
        print(user)
        for u in user:
            if email == u.email:
                if password == u.password:
                    messages.success(request, 'you are logged in')
                    request.session['email']=email
                    u_id=u.id

                    return redirect('farmers')
                else:
                    messages.warning(request, 'wrong password')
                    return redirect('login_farmer')
            else:
                messages.warning(request, 'Invalid Credentials')
                return redirect('login_farmer')
    return render(request, 'authentication/login_farmer.html')

def login_trader(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = trader_auth.objects.filter(email__iexact=email)
        print(user)
        for u in user:
            if email == u.email:
                if password == u.password:
                    messages.success(request, 'you are logged in')
                    request.session['email']=email
                    request.session['id']=u.id
                    
                    u_id=u.id
                    return redirect('traders')
                else:
                    messages.warning(request, 'wrong password')
                    return redirect('login_trader')
            else:
                messages.warning(request, 'Invalid Credentials')
                return redirect('login_trader')
    return render(request, 'authentication/login_trader.html')



def farmer_register(request):
    if request.method == 'POST':
            first_name = request.POST.get('first_name', False)
            last_name = request.POST.get('last_name', False)
            email = request.POST.get('email', False)
            password = request.POST.get('password', False)
            confirm_password = request.POST.get('confirm_password', False)
            address = request.POST.get('address', False)
            state = request.POST.get('state', False)
            city = request.POST.get('city', False)
            phone = request.POST['phone']
            photo = request.POST['url']
            

            
            messages.success(request, "File upload in Firebase Storage successful")
        
            
            users = farmer_auth(first_name = first_name, last_name = last_name, email = email, password=password, address=address, confirm_password=confirm_password, state=state, city=city, phone=phone, photo=photo)

            users.save()

            messages.success(request, 'Account created successfully')
            return redirect('login_farmer')

            
    return render(request, 'authentication/farmer_register.html')     

        
        
            
                

def trader_register(request):
    if request.method == 'POST':
            name = request.POST.get('name', False)
            company_name = request.POST.get('company_name', False)
            email = request.POST.get('email', False)
            password = request.POST.get('password', False)
            confirm_password = request.POST.get('confirm_password', False)
            address = request.POST.get('address', False)
            state = request.POST.get('state', False)
            city = request.POST.get('city', False)
            phone = request.POST['phone']
            photo = request.POST['url']
            
            users = trader_auth(name = name, email = email, company_name = company_name, password=password, confirm_password=confirm_password, address=address, state=state, city=city, phone=phone, photo=photo)

            users.save()

            messages.success(request, 'Account created successfully')
            return redirect('login_trader')

    return render(request, 'authentication/trader_register.html')        


def logout_user(request):
    logout(request)
    return redirect('index')