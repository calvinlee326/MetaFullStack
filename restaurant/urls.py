from django.urls import path, include
from .views import *


urlpatterns = [
    path('menu-items/', MenuItemView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item'),
    # path('booking/', BookingView.as_view(), name='booking'),
]
