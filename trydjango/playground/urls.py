from django.urls import path
from . import views

urllpatterns = [
    path('hello/', views.say_hello)
]