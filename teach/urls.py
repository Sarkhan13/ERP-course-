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
    path('student/', studentpage, name='student'),
    path('student/add/', student_create, name='student_create'),
    path('student/<int:id>/update', student_update, name='student_update'),
    path('student/<int:id>/delete', student_delete, name='student_delete'),
    path('journal/', journalpage, name='journal'),
    path('task/',taskpage, name='task'),
    path('task/<int:id>/detail', taskdetail, name='task_detail'),
    path('task/create/', task_create, name='task_create'),
    path('task/<int:id>/update', task_update, name='task_update'),
    path('task/<int:id>/delete', task_delete, name='task_delete'),
    path('payments/', paypage, name='pay'),
    path('payment/create',pay_create, name='pay_create'),
    path('pay/<int:id>/update', pay_update, name='pay_update'),
    path('pay/<int:id>/delete', pay_delete, name='pay_delete'),
    path('chek/', checks, name='checks'),
    path('chek/<int:id>/update', chek_update, name='chek_update'),
    path('chek/create',check_for, name='chek_create'),
    
]