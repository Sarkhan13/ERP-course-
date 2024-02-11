import schedule
import time
from datetime import datetime, timedelta
from django.utils import timezone
from .models import chek,pay




def chek_create():
    today = timezone.now()
    
    pay_day = today - timedelta(days=12)
    
    pays =pay.objects.all()

    post = pay.objects.filter(started_date=pay_day)

    checks = chek.objects.filter(created_date__gte=pay_day)
 
    if post:
        for p in post:

            chek.objects.create(paymnt = p, payment_date = today)
            print('working for new one')
            print(checks)

    if checks:
        
        for pa in pays:
            
            for c in pa.cheks.all():
                
                if c.created_date == pay_day:
                    

                    chek.objects.create(paymnt = pa, payment_date = today)
                    print('working for old one')


    print('Periodic task executed!')

