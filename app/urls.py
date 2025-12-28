from django.urls import path
from .views import ShortenURLView, redirect_view

urlpatterns = [
    path('api/shorten/', ShortenURLView.as_view(), name='shorten'),
    path('<str:code>/', redirect_view, name='redirect'),
]
