from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'vendor'

urlpatterns = [
    path('register/', views.VendorRegisterView.as_view(), name='register'),
    path('login/', views.VendorLoginView.as_view(), name='login'),
    # path('logout/', views.vendor_logout, name='logout'),
    path('dashboard/', views.VendorDashboardView.as_view(), name='dashboard'),
    path('signup/', views.api_register_view, name='api_register'),
    # path('api-login/', views.api_login_view, name='api_login'),
    
]
