
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('admin-panel/', include('admin_panel.urls')),  # Include admin panel URLs
    
]
