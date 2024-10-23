# herodialogue/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('maheshbabu/', views.func1, name='maheshbabu'),
    path('balayaaa/', views.func2, name='balayaaa'),
    path('ntr/', views.func3, name='ntr'),
]
