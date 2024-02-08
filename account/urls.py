from django.urls import path
from .views import *



urlpatterns = [
    path('login/', loginpage, name='login'),
]