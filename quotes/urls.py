from django.urls import path
from .views import home,about,add_stock,delStock,delete_stock

app_name = 'quotes'

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('add-stock/',add_stock,name='add_stock'),
    path('delete/<int:pk>',delStock, name='del_stock'),
    path('delete_stock',delete_stock,name='delete_stock'),

]
