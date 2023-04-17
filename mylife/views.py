from django.shortcuts import render,HttpResponse
from mylife.models import Mylife
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def mylife(request):
    if request.method=='POST':
        age=request.POST.get('age')
        topic=request.POST.get('topic')
        college=request.POST.get('college')
        school=request.POST.get('school')
        rollno=request.POST.get('rollno')
        mylife=Mylife(age=age,topic=topic,college=college,school=school,rollno=rollno)
        mylife.save()
    return render(request,'life.html')

def show(request):
    mylife=Mylife.objects.all().values()
    template=loader.get_template('show.html')
    context={
        'mylife':mylife
    }
    return HttpResponse(template.render(context,request))# only to show data on table through show.html

def delete(request,id):
    mylife=Mylife.objects.get(id=id)
    mylife.delete()
    return HttpResponseRedirect(reverse('show'))

def update(request,id):
    mylife=Mylife.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        'mylife':mylife
    }
    return HttpResponse(template.render(context,request))# only to run update function

def updaterecord(request,id):
    age=request.POST['age']
    topic=request.POST['topic']
    college=request.POST['college']
    school=request.POST['school']
    rollno=request.POST['rollno']
    mylife=Mylife.objects.get(id=id)
    mylife.age=age
    mylife.topic=topic
    mylife.college=college
    mylife.school=school
    mylife.rollno=rollno
    mylife.save()
    return HttpResponseRedirect(reverse('show'))# this register we is from our first function and this complatae 

