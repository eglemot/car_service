from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('orders/my', views.OrderListView.as_view(), name='user_orders'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order'),
    path('cars/', views.ModelMakeListView.as_view(), name='cars'),
    path('orders/my/new', views.UserOrderLineCreateView.as_view(), name='add_order_line'),
    path('orders/my/line/<int:pk>/delete/', views.UserOrderLineDeleteView.as_view(), name='delete_order_line'),
]