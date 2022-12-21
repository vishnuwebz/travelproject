from django.shortcuts import render
from . models import Languages,Programmers
# Create your views here.
def demo(request):
    obj=Languages.objects.all()
    obj1=Programmers.objects.all()
    return render(request,"index.html",{'language':obj,'programmer':obj1})