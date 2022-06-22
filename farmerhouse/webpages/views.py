from django.shortcuts import render
from .models import crop_details

# Create your views here.

def index(request):
    crops = crop_details.objects.all()
    data = {
        'crops': crops,
    }
    return render(request, 'webpages/index.html', data)