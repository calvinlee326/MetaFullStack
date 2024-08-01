from django.urls import path, include
from .views import MenuView, BookingView, SingleMenuItemView


urlpatterns = [
    path('menu/', MenuView.as_view(), name='menu'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item'),
    path('booking/', BookingView.as_view(), name='booking'),
]
