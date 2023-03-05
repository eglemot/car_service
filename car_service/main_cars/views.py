from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.views import generic
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from . forms import OrderCommentForm
from . forms import OrderLineForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

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

class OrderListView(LoginRequiredMixin, generic.ListView):
    model = models.Order
    paginate_by = 4
    template_name = 'main_cars/order_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(car__client=self.request.user)
        return qs

class ModelMakeListView(generic.ListView):
    model = models.ModelMake
    paginate_by = 6
    template_name = 'main_cars/auto_list.html'

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

class OrderDetailView(generic.edit.FormMixin, generic.DetailView):
    model = models.Order
    template_name = 'main_cars/order_details.html'
    form_class = OrderCommentForm

    def get_success_url(self) -> str:
        return reverse('order', kwargs={'pk': self.get_object().id})

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['order'] = self.get_object()
        initial['client'] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.client = self.request.user
        form.save()
        messages.success(self.request, 'Comment posted successfully')
        return super().form_valid(form)

class UserOrderLineDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
     model = models.OrderLine
     template_name = 'main_cars/delete_order_line.html'

     def get_success_url(self) -> str:
         return reverse_lazy('order', kwargs = {'pk': self.get_object().order.pk})

     def test_func(self):
         return self.get_object().order.car.client == self.request.user

     def form_valid(self, form):
         messages.success(self.request, _('Successfully deleted order line'))
         return super().form_valid(form)

class UserOrderLineCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.OrderLine
    template_name = 'main_cars/add_order_line.html'
    form_class = OrderLineForm
    success_url = reverse_lazy('user_orders')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['status'] = 'n'
        return initial

    def form_valid(self, form):
        form.instance.client = self.request.user
        form.instance.status = 'n'
        messages.success(self.request, f' successfully created new order line: {form.instance}')
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['client'] = self.request.user
        return kwargs




    
