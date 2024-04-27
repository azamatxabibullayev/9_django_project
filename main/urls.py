from django.urls import path
from mains.views import main

urlpotterns = [
    path('main', main)
]
