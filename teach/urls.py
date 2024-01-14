from django.urls import path,include
from .views import *


urlpatterns = [
    path('', teachers, name='teach'),
    path('<int:id>/detail', teacher_detail, name='teachdetail'),
    path('search/', searching, name='search'),
    path('groups/', grouppage, name='group'),
    path('group/<int:id>/detail', groupdetail, name='groupdetail'),
    path('add/', teacher_add, name='teacher_add'),
    path('group/add/', group_add, name='group_add'),
    path('<int:id>/update', teacher_update, name='teacher_update'),
    path('<int:id>/delete', teacher_delete, name='teacher_delete'),
    path('group/<int:id>/update', group_update, name='group_update'),
    path('group/<int:id>/delete', group_delete, name='group_delete'),
    
]