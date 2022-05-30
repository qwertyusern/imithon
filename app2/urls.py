from django.urls import path
from .views import *

urlpatterns = [
    path('asosiy/', AsosiyView.as_view(), name="asosiy"),
    path('sarlavha/<int:pk>', SarlavhaView.as_view(), name="sarlavha"),
]