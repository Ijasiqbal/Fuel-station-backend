from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.credit_transaction_list, name='credit-transaction-list'),
    path('transactions/<int:pk>/', views.credit_transaction_detail, name='credit-transaction-detail'),
]
