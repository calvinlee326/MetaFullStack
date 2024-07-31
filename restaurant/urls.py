from django.urls import path, include
from .views import MenuView, BookingView

urlpatterns = [
    path('menu/', MenuView.as_view(), name='menu'),
    path('booking/', BookingView.as_view(), name='booking'),
]
