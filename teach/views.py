from django.shortcuts import render
from .models import teacher

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
