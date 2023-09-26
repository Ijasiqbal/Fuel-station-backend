from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reading.urls')),
    path('api/', include('employee.urls')),  
    path('api/', include('transactions.urls')), 
    path('api/', include('creditors.urls')),
    path('api/', include('prices.urls')),
]
