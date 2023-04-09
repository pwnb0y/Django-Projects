from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            #fm.save
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email'] 
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
    else:
        fm = StudentRegistration()

    return render(request, 'enroll/addandshow.html',{'form':fm})