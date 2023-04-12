from django.shortcuts import render

# Create your views here.
def conditions(request):


    d={'a':190 ,'b':20, 'c':200}
    return render(request,'conditions.html',context=d)