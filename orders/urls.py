from django.urls import URLPattern, path
from . import views

app_name = 'orders'


URLPattern=[
    path('create/', views.order_create , name = 'order_create')
]