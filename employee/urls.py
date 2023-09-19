from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee_list),
    path('employee/<int:pk>/', views.employee_detail),
]
