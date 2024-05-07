from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from django.http import HttpResponse
from .models import User
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
#This function will Add new items and show all data
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            epa = make_password(pw)

            
            reg = User(name=nm, email=em, password=epa)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})

#This function will update/edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
          fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request, 'enroll/updatestudent.html', {'form':fm})



#this function will delete the added items
def delete_data(request, id):
    if request.method == 'POST':
     pi = User.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect('/')