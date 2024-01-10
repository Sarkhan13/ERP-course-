from django.urls import path,include
from .views import *


urlpatterns = [
    path('', teachers, name='teach'),
    path('<int:id>/detail', teacher_detail, name='teachdetail'),
    path('search/', searching, name='search'),
    
]