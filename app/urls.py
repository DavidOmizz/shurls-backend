from django.urls import path
from .views import ShortenURLView, redirect_view, pings

urlpatterns = [
    path('api/shorten/', ShortenURLView.as_view(), name='shorten'),
    path('pings/', pings, name='pings'),
    path('<str:code>/', redirect_view, name='redirect'),
]
