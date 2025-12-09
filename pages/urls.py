from django.urls import path
from .views import get_homepage

urlpatterns = [
    path('', get_homepage, name='homepage')
]