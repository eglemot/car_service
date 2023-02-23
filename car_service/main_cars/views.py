from django.shortcuts import render
from . import models
from django.shortcuts import render
from django.views import generic

def index(request):
    order_count = models.Order.objects.count()
    return render(request, 'main_cars/index.html', {
        'order_count': order_count,
    })

def services(request):
    services = models.Service.objects.all()
    return render(request, 'main_cars/service_list.html', {
        'services': services,
    })

class OrderListView(generic.ListView):
    model = models.Order
    template_name = 'main_cars/order_list.html'

class OrderDetailView(generic.DetailView):
    model = models.Order
    template_name = 'main_cars/order_details.html'