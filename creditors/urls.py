# creditors/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('creditors/', views.creditor_list, name='creditor-list'),
    path('creditors/<int:pk>/', views.creditor_detail, name='creditor-detail'),
]
