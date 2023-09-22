from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_panel, name='admin_panel'),
    path('edit-app/<int:pk>/', views.edit_app, name='edit_app'),  # Example URL pattern
    path('delete-app/<int:pk>/', views.delete_app, name='delete_app'),  # Example URL pattern
    
]
