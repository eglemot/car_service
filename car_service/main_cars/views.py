from django.shortcuts import render
from . import models

def index(request):
    order_count = models.Order.objects.count()
    return render(request, 'main_cars/index.html', {
        'order_count': order_count,
    })
    
