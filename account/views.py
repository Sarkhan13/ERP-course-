from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import login_form
from teach.views import studentpage,teachers
from teach.models import student,chek,journal
from django.shortcuts import get_object_or_404
from django.contrib import messages



def loginpage(request):
    
    form = login_form()

    if request.method == 'POST':
        form = login_form(request.POST or None)

        if form.is_valid():
            user  = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])

            if user:
                login(request, user)

                if user.student_user.all() != "":
                    for stud in user.student_user.all():
                            
                        return redirect(stud.get_url)
                
                return redirect(teachers)    
                
                
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
    






