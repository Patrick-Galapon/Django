# portfolio_app/urls.py

from django.urls import path
from portfolio_app import views

urlpatterns = [
    path("", views.home, name='home'),
]