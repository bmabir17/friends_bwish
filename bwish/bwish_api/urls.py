from django.urls import path, re_path
from django.conf.urls import include
from . import views

app_name = 'bwish_api'

urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    path('customer/register', views.submit_customer_register, name='api/submit_customer_register'),

]