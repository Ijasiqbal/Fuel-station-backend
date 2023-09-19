from django.urls import path
from .views import reading_list, reading_detail

urlpatterns = [
    path('readings/', reading_list, name='reading-list'),
    path('readings/<int:pk>/', reading_detail, name='reading-detail'),
]
