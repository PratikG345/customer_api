from django.urls import path
from .views import get_customer,add_customer,get_order,add_order,order_detail

urlpatterns = [
    # Customer urls
    path('customers/',get_customer,name="get_customer"),
    path('customers/add',add_customer,name="add_customer"),
    
    # Order urls
    path('orders/',get_order,name="get_order"),
    path('orders/add',add_order,name="add_order"),
    path('orders/<int:pk>',order_detail,name="order_detail"),
    
    
]
