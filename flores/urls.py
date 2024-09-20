from django.urls import path
from . import views

urlpatterns = [
    path('flores/', views.flores),
]