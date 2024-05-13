from django.urls import path
from . import views

urlpatterns = [
    path('valid_moves/<slug:piece>/', views.valid_moves, name='valid_moves'),
]