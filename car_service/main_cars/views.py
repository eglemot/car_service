from django.shortcuts import render
from . import models
from django.shortcuts import render
from django.views import generic
from django.db.models import Q

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
    paginate_by = 4
    template_name = 'main_cars/order_list.html'

    def get_queryset(self):
        qs =  super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            qs = qs.filter(
                Q(car__customer__icontains=query)
            )
        return qs

class ModelMakeListView(generic.ListView):
    model = models.ModelMake
    paginate_by = 6
    template_name = 'main_cars/auto_list.html'

    def get_queryset(self):
        qs =  super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            qs = qs.filter(
                Q(model__istartswith=query) | Q(make__istartswith=query)
            )
        return qs

class OrderDetailView(generic.DetailView):
    model = models.Order
    template_name = 'main_cars/order_details.html'