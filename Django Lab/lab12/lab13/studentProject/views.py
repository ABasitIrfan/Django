from django.shortcuts import render, redirect
from .forms import stdForm
from.models import student

# Create your views here.


def std_show(request):
    std_list = {'student_list' :student.objects.all()}
    return render(request,'studentProject/show.html',std_list)


def std_insert (request,id=0):
    if request.method == 'GET':
        if id==0:
            form = stdForm()
        else :
            std = student.objects.get(pk=id)
            form = stdForm(instance=std)
        return render(request, 'studentProject/insert.html', {'form': form})
    else :
        if id==0:
            form = stdForm(request.POST)
        else :
            std = student.objects.get(pk=id)
            form = stdForm(request.POST, instance=std)
    if form.is_valid():
        form.save()
    return redirect('show/')



def std_delete (request,id):
    std=student.objects.get(pk=id)
    std.delete()
    return redirect('../show/')
