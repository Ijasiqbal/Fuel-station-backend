from django.urls import path
from .views import PriceList, PriceDetail

urlpatterns = [
    path('prices/', PriceList.as_view(), name='price-list'),
    path('prices/<int:pk>/', PriceDetail.as_view(), name='price-detail'),
]
