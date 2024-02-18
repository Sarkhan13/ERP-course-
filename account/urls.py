from django.urls import path
from .views import *



urlpatterns = [
    path('login/', loginpage, name='login'),
    path('stud/<int:id>/panel/', student_panel, name='stud_panel'),
    path('logout/', logout_func, name='logout' ),
    path('dash/', analys_page, name='analys'),
    
]