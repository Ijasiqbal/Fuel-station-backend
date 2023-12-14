from django.urls import path
from .views import (
    SalesListCreateView,
    SalesDetailView,
    CustomClosingSalesCreateView,
)

urlpatterns = [
    path('sales/', SalesListCreateView.as_view(), name='sales-list-create'),
    path('sales/<int:pk>/', SalesDetailView.as_view(), name='sales-detail'),

    path('closingSales/', CustomClosingSalesCreateView.as_view(), name='closing-sales-list-create'),
]
