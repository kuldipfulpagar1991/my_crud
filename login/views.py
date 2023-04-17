from django.shortcuts import render, reverse
from django.shortcuts import HttpResponseRedirect
from .forms import Myform

# Create your views here.
def login(request):
    if request.method=='POST':
        form = Myform(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('show'))
        else:
            return render(request,'show.html')
    else:
        form=Myform()
        return render(request,'login.html',{'form':form})