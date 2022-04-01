from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_transaction', views.new_transaction, name='new_transaction'),
    path('transactions', views.transactions, name='transactions'),
]
