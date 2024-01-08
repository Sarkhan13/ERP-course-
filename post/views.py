from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')


def teachers(request):
    return render(request,'teacher.html' )
