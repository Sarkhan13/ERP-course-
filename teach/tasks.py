import schedule
import time
from datetime import datetime, timedelta
from django.utils import timezone
from .models import chek,pay
from django.db.models import Q



def chek_create():
    today = timezone.now()
    
    pay_day = today - timedelta(days=31)

    hay_day = today - timedelta(days=29)
    
    pays =pay.objects.all()

    post = pay.objects.filter(started_date=pay_day)

    checks = chek.objects.filter(created_date__gte=pay_day)
 
    if post:
        for p in post:

            chek.objects.create(paymnt = p, payment_date = today)
            print('working for new one')
            

    if checks:
        
        for pa in pays:
            
            final = chek.objects.filter(Q(created_date__gte=pay_day) & Q(created_date__lte=hay_day) & Q(paymnt = pa))
            
            if final:
                chek.objects.create(paymnt = pa, payment_date = today)
                print('working for new one')
                
                


    print('Periodic task executed!')

