from .models import student,month_statistic
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q




def for_chart():
    today = timezone.now()

    first_day_month = today - timedelta(days=30)

    stud_count = student.objects.filter(Q(created_date__gte = first_day_month) & Q(created_date__lte = today)).count()

    first_stud = student.objects.filter(Q(created_date__gte = first_day_month) & Q(created_date__lte = today))[0]

    monthly = first_stud.created_date.date()

    current_stat = month_statistic(student_count=stud_count, month=monthly)

    current_stat.save()

    