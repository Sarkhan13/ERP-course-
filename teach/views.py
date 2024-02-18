from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import Http404
from .models import *
from .forms import *
from django.contrib.auth.models import User
from .tasks import chek_create
from django.db.models import F 





def teachers(request):
    teachers = teacher.objects.all()

    for teac in teachers:

        if not request.user.is_staff and request.user != teac.user:
            raise Http404
        
        contex = {
                'teachers':teachers,
            }

        return render(request, 'teacher.html',contex)



def teacher_detail(request, id):
    teach = teacher.objects.get(id=id)

    if request.user.is_staff or request.user == teach.user:

        contex  = {
            'teach': teach,
        }

        return render(request, 'teachdetail.html', contex)
    else:
        raise Http404



def valid_query(query):
    return query !="" and query is not None

def searching(request):
    searchdata = request.GET['query']
    teachers = teacher.objects.all()
    pays = pay.objects.all()

    if valid_query(searchdata):
        teachers = teacher.objects.filter(name__contains = searchdata)

    if valid_query(searchdata):
        pays = pay.objects.filter(student__name__icontains =searchdata)

    contex = {
        'teachers':teachers,
        'pays': pays,
        'searchdata': searchdata,
    }

    return render(request, 'result.html', contex)



def grouppage(request):
    groups = group.objects.all()

    for grup in groups:

        if not request.user.is_staff and request.user != grup.teach.user:
            raise Http404
            
        contex = {
                'groups': groups,
            }

        return render(request, 'groups.html',contex)



def groupdetail(request, id):
    groups= get_object_or_404(group, id=id)

    if request.user.is_staff or request.user == groups.teach.user:
    
        contex = {
            'group':groups,
            }

        return render(request, 'groupdetail.html', contex)
    else:
        raise Http404



def teacher_add(request):
    if not request.user.is_staff:
        raise Http404
        
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
    if not request.user.is_staff:
        raise Http404
    
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
    if not request.user.is_staff:
        raise Http404
    
    post = get_object_or_404(teacher, id=id)

    post.delete()

    return redirect(teachers)



def group_add(request):
    if not request.user.is_staff:
        raise Http404
    
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
    if not request.user.is_staff:
        raise Http404
    
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
    if not request.user.is_staff:
        raise Http404
    
    post = get_object_or_404(group, id=id)

    post.delete()

    return redirect(grouppage)



def studentpage(request):
    students = student.objects.all()

    for stud in students:

        if not request.user.is_staff and request.user != stud.user:
            raise Http404
        

    contex = {
            'students': students,
        }


    return render(request, 'student.html', contex)



def student_create(request):
    if not request.user.is_staff:
        raise Http404
    
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
    if not request.user.is_staff:
        raise Http404
    
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
    if not request.user.is_staff:
        raise Http404
    
    post = get_object_or_404(student, id=id)

    post.delete()

    return redirect(studentpage)
    


def journalpage(request):
    
    groups = group.objects.all()

    students = student.objects.all()

    journals = journal.objects.all()

    dates = date.objects.all().order_by('date_time')

    for jour in journals:
        if not request.user.is_staff and jour.student.group.teach.user != request.user: 
            raise Http404


        contex = {
            'groups': groups,
            'students': students,
            'journals': journals,
            'dates': dates,
        }


        return render(request, 'journal.html',contex)   


def taskpage(request):
    
    tasks = task.objects.all().order_by('created_date')

    for tas in tasks:
        if not request.user.is_staff and tas.teacher.user != request.user: 
            raise Http404

        context = {
            'tasks': tasks,
        }


        return render(request, 'task.html',context) 



def taskdetail(request, id):
    
    data = task.objects.get(id=id)

    studs = data.group.student_set.all()

    for stud in studs:

        if request.user.is_staff or request.user == data.teacher.user or request.user == stud.user:

            context = {
                'task': data,
            }

            return render(request, 'taskdetail.html', context)
        else:
            raise Http404



def task_create(request):
    teachs = request.user.teacher_user.first()
    
    if not request.user.is_staff and not teachs:
        raise Http404
        
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
    teachs = request.user.teacher_user.first()

    post = get_object_or_404(task, id=id)
    
    if not request.user.is_staff and not teachs and not post.teacher.user:
        raise Http404
    

    form = task_form(request.POST or None, instance=post)

    if form.is_valid():
        form.save()

        return redirect(taskpage)
        
    context = {
            'form': form,
        }

    return render(request, 'foradd.html', context)


def task_delete(request, id):
    teachs = request.user.teacher_user.first()

    post = get_object_or_404(task, id=id)
    
    if not request.user.is_staff and not teachs and not post.teacher.user:
        raise Http404


    post.delete()

    return redirect(taskpage)



def paypage(request):
    if not request.user.is_staff:
        raise Http404
    
    payments = pay.objects.all()

    context = {
            'payments': payments,
        }

    return render(request, 'pay.html', context)



def pay_create(request):
    if not request.user.is_staff:
        raise Http404
    
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
    if not request.user.is_staff:
        raise Http404
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
    if not request.user.is_staff:
        raise Http404
    
    post = get_object_or_404(pay, id=id)

    post.delete()

    return redirect(paypage)

                      
    

def checks(request):
    if not request.user.is_staff:
        raise Http404
    
    all_cheks = chek.objects.all().order_by('payed').order_by('-created_date')

    context = {
        'cheks': all_cheks,
        }

    return render(request, 'checks.html', context)


def check_for(request):
    if not request.user.is_staff:
        raise Http404
    chek_create()
        
    return HttpResponse('Əməliyyat uğurla həyata keçdi!')



def chek_update(request,id):
    if not request.user.is_staff:
        raise Http404
    post = get_object_or_404(chek, id=id)

    form = check_form(request.POST or None, instance=post)

    if form.is_valid():
        form.save()

        return redirect(checks)
        
    context = {
        'form': form, 
        }

    return render(request, 'foradd.html',context)









    


        

    

