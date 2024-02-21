from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import login_form
from teach.views import teachers,paypage
from teach.models import student,chek,journal
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import Http404
from django .utils import timezone
from django.db.models import Q
from datetime import timedelta
from teach.tasks2 import for_chart




def for_chart_func(request):
    for_chart()
    return HttpResponse('successfully!')




def loginpage(request):
    
    form = login_form()

    if request.method == 'POST':
        form = login_form(request.POST or None)

        if form.is_valid():
            user  = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])

            if user:
                login(request, user)

                if request.user.is_superuser:
                    return redirect(analys_page)

                elif request.user.student_user.all() != "":
                    for stud in request.user.student_user.all():
                            
                        return redirect(stud.get_url)
            else:
                messages.error(request, 'Username və ya şifr yanlışdır!')    
                
                
    context = {
            'form':form,
        }

    return render(request, 'login.html', context)



def logout_func(request):
    logout(request)
    return redirect(loginpage)



def student_panel(request,id):
    
    stud = get_object_or_404(student, id=id)

    fies = chek.objects.filter(paymnt__student = stud)

    for fie in fies:
        if fie.payed == False:
                messages.error(request, 'Sizin aylıq ödənişiniz vaxtı çatıb. Zəhmət olmasa kursa yaxınlaşıb ödənişinizi edərdiniz.')

    jours = journal.objects.filter(student = stud)
    
    context = {
        'stud':stud,
        'jours': jours,   
    }

    return render(request, 'students.html', context)
    


def analys_page(request):
    if not request.user.is_superuser:
        raise Http404
    
    students = student.objects.all()

    today = timezone.now()

    last_month = today - timedelta(days=30)

    other_tm = today - timedelta(days=0)

    jours = journal.objects.filter(Q(date__date_time=today) & Q(existence=True))

    jour = journal.objects.filter(Q(date__date_time=today) & Q(existence=False))

    checks = chek.objects.all()

    profit = 0

    for check in checks:
        if check.payed == True:
            profit += check.paymnt.monthly_payment 

    lastmonth = 0

    fies = chek.objects.filter(Q(created_date__gte=last_month) & Q(created_date__lte=other_tm) & Q(payed=True))

    if fies:
        for fi in fies:
            lastmonth += fi.paymnt.monthly_payment  

    
    context = {
        'students': students,
        'jours':jours,
        'jour': jour,
        'profit':profit,
        'lastmonth': lastmonth,
       
    }

    return render(request, 'index.html',context)










