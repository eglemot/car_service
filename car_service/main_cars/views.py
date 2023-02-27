from django.shortcuts import render
from . import models
from django.views import generic
from django.db.models import Q
from datetime import date

def index(request):
    order_count = models.Order.objects.count()
    request.session['visit_count'] = request.session.get('visit count', 0) + 1
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

    # views.py

class ModelMakeListView(generic.ListView):
    model = models.ModelMake
    paginate_by = 6
    template_name = 'main_cars/auto_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        year_from_filter = self.request.GET.get('year_from')
        year_to_filter = self.request.GET.get('year_to')
        if year_from_filter and year_to_filter:
            qs = qs.filter(year__range=(year_from_filter, year_to_filter))
        elif year_from_filter:
            qs = qs.filter(year__gte=year_from_filter)
        elif year_to_filter:
            qs = qs.filter(year__lte=year_to_filter)
        query = self.request.GET.get('search')
        if query:
            qs = qs.filter(
                Q(model__istartswith=query) | Q(make__istartswith=query)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        years = [(year, year) for year in range(1999, 2024)]
        context['years'] = years
        return context

class OrderDetailView(generic.DetailView):
    model = models.Order
    template_name = 'main_cars/order_details.html'