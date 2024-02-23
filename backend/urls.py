from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reading.urls')),
    path('api/', include('employee.urls')),  
    path('api/', include('transactions.urls')), 
    path('api/', include('creditors.urls')),
    path('api/', include('prices.urls')),
    path('api/', include('sales.urls')),
    path('api-auth/', include('LoginApp.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
