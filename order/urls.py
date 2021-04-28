from django.urls import path
from .views import OrderListCreateView, OrderView


urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderView.as_view(), name='order'),
]
