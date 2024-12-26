from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_advertisement, name='add_advertisement'),
    path('', views.list_ads, name='list_ads'),
]
