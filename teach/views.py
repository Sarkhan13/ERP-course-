from django.shortcuts import render,redirect,get_object_or_404
from .models import teacher,group
# from django.db.models import Count
from .forms import teacher_form,group_form
from django.contrib.auth.models import User

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
            post.teacher = User.objects.get(id=1)
            post.save()

            return redirect(teachers)

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

        return redirect(teachers)

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

        return redirect(grouppage)

    contex = {
        'form': form,
    } 


    return render(request, 'foradd.html',contex)    



def group_delete(request,id):
    post = get_object_or_404(group, id=id)

    post.delete()

    return redirect(grouppage)

    