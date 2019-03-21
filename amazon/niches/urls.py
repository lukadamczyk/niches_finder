from django.urls import path
from . import views


urlpatterns = [
    path('niches/', views.niches, name='niches'),
]