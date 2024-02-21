from django.urls import path
from .views import *



urlpatterns = [
    path('', loginpage, name='login'),
    path('stud/<int:id>/panel/', student_panel, name='stud_panel'),
    path('logout/', logout_func, name='logout' ),
    path('dash/', analys_page, name='analys'),
    path('chart/',for_chart_func, name='chartss'),
    
]