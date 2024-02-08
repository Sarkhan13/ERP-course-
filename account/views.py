from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import login_form
from teach.views import studentpage



def loginpage(request):
    form = login_form()

    if request.method == 'POST':
        form = login_form(request.POST or None)

        if form.is_valid():
            user  = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])

            if user:
                login(request, user)
                return redirect(studentpage)
            
    context = {
        'form':form,
    }

    return render(request, 'foradd.html', context)
    






