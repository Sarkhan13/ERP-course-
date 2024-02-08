from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import *
# from django.db.models import Count
from .forms import *
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
import time
from .tasks import chek_create






def teachers(request):
    teachers = teacher.objects.all()


    contex = {
        'teachers':teachers,
        
    }

    return render(request, 'teacher.html',contex)


def teacher_detail(request, id):
    teach = teacher.objects.get(id=id)

    contex  = {
        'teach': teach,
    }

    return render(request, 'teachdetail.html', contex)

def valid_query(query):
    return query !="" and query is not None

def searching(request):
    searchdata = request.GET['query']
    teachers = teacher.objects.all()

    if valid_query(searchdata):
        teachers = teacher.objects.filter(name__contains = searchdata)


    contex = {
        'teachers':teachers,
        'searchdata': searchdata,
    }

    return render(request, 'result.html', contex)


def grouppage(request):
    groups = group.objects.all()

    contex = {
        'groups': groups,
    }

    return render(request, 'groups.html',contex)



def groupdetail(request, id):
    groups = group.objects.get(id=id)

    contex = {
        'group':groups,
    }


    return render(request, 'groupdetail.html', contex)



def teacher_add(request):
    form = teacher_form()

    if request.method == 'POST':
        form = teacher_form(request.POST or None,request.FILES or None)

        if form.is_valid():
            post = form.save(commit=False)
            usern = f'{post.name}12'
            new_user = User(username=usern)
            new_user.set_password('Admin12!')
            new_user.save()
            post.user = new_user
            post.save()

            return redirect(post.get_url)

    else:
        form = teacher_form()

    contex = {
        'form': form,
    } 


    return render(request, 'foradd.html',contex)


def teacher_update(request, id):
    post = get_object_or_404(teacher, id=id)

    form = teacher_form(request.POST or None,request.FILES or None,instance=post)

    if form.is_valid():
        form.save()

        return redirect(post.get_url)

    contex = {
        'form': form,
    } 

    return render(request, 'foradd.html',contex)


def teacher_delete(request, id):
    post = get_object_or_404(teacher, id=id)

    post.delete()

    return redirect(teachers)



def group_add(request):
    form = group_form()

    if request.method == 'POST':
        form = group_form(request.POST or None)

        if form.is_valid():
            form.save()

            return redirect(grouppage)

    else:
        form = group_form()

    contex = {
        'form': form,
    } 


    return render(request, 'foradd.html',contex)



def group_update(request, id):
    post = get_object_or_404(group, id=id)

    form = group_form(request.POST or None,instance=post)

    if form.is_valid():
        form.save()

        return redirect(post.get_url)

    contex = {
        'form': form,
    } 


    return render(request, 'foradd.html',contex)    



def group_delete(request,id):
    post = get_object_or_404(group, id=id)

    post.delete()

    return redirect(grouppage)



def studentpage(request):
    students = student.objects.all()

    contex = {
        'students': students
    }


    return render(request, 'student.html', contex)



def student_create(request):
    form = student_form()

    if request.method == 'POST':
        form = student_form(request.POST or None,request.FILES or None)

        if form.is_valid():
            post = form.save(commit=False)
            
            usern = f'{post.name}123'
            
            new_user = User(username=usern)
            new_user.set_password('Admin123!')
            new_user.save()
            
            post.user = new_user
            post.save()            


            return redirect(studentpage)
        
    else:
        form = student_form()

    contex = {
        'form': form,
    } 


    return render(request, 'foradd.html',contex)



def student_update(request,id):
    post = get_object_or_404(student, id=id)

    form = student_form(request.POST or None,request.FILES or None,instance=post)

    if form.is_valid():
        form.save()

        return redirect(studentpage)
    

    contex = {
        'form': form,
    } 


    return render(request, 'foradd.html',contex)



def student_delete(request,id):
    post = get_object_or_404(student, id=id)

    post.delete()

    return redirect(studentpage)
    


def journalpage(request):
    groups = group.objects.all()

    students = student.objects.all()

    journals = journal.objects.all()

    dates = date.objects.all().order_by('date_time')

    contex = {
        'groups': groups,
        'students': students,
        'journals': journals,
        'dates': dates,
    }


    return render(request, 'journal.html',contex)   


def taskpage(request):
    tasks = task.objects.all().order_by('created_date')

    context = {
        'tasks': tasks,
    }


    return render(request, 'task.html',context) 



def taskdetail(request, id):
    data = task.objects.get(id=id)

    context = {
        'task': data,
    }

    return render(request, 'taskdetail.html', context)



def task_create(request):
    form = task_form()

    if request.method == 'POST':
        form = task_form(request.POST or None)

        if form.is_valid():
            form.save()

            return redirect(taskpage)

    else:
        form = task_form()

    context = {
        'form':form,
    }

    return render(request, 'foradd.html',context)



def task_update(request, id):
    post = get_object_or_404(task, id=id)

    form = task_form(request.POST or None, instance=post)

    if form.is_valid():
        form.save()

        return redirect(taskpage)
    
    context = {
        'form': form,
    }

    return render(request, 'foradd.html', context)


def task_delete(request, id):
    post = get_object_or_404(task, id=id)

    post.delete()

    return redirect(taskpage)



def paypage(request):
    payments = pay.objects.all()

    context = {
        'payments': payments,
    }

    return render(request, 'pay.html', context)



def pay_create(request):
    form = pay_form()

    if request.method == 'POST':
        form = pay_form(request.POST or None)

        if form.is_valid():
            form.save()

            return redirect(paypage)
        
    else:
        form = pay_form()

    context = {
        'form': form,
    }

    return render(request, 'foradd.html', context)



def pay_update(request, id):
    post = get_object_or_404(pay, id=id)

    form = pay_form(request.POST or None, instance=post)

    if form.is_valid():
        form.save()

        return redirect(paypage)

    context = {
        'form': form,
    }

    return render(request, 'foradd.html', context)



def pay_delete(request, id):
    post = get_object_or_404(pay, id=id)

    post.delete()

    return redirect(paypage)

                      
    

def checks(request):
    
    all_cheks = chek.objects.all().order_by('payed')

    context = {
       'cheks': all_cheks,
    }

    return render(request, 'checks.html', context)


def check_for(request):
    chek_create()
    
    return render(request,'checks.html')



def chek_update(request,id):
    post = get_object_or_404(chek, id=id)

    form = check_form(request.POST or None, instance=post)

    if form.is_valid():
        form.save()

        return redirect(checks)
    
    context = {
       'form': form, 
    }

    return render(request, 'foradd.html',context)









    


        

    

