from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    value1=request.POST['number1']
    value2=request.POST['number2']
    res=value1+value2
    return render(request,'result.html',{'result':res})