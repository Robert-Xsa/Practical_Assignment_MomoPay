from django.urls import path
from purchases import views

urlpatterns = [
    path('add_invoice/', views.add_invoice, name='add_invoice'),
]
