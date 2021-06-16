from django.urls import path
from .views import OrderListCreateView, OrderView, FacebookLogin


urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderView.as_view(), name='order'),
    path('api/<version>/rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),

]
