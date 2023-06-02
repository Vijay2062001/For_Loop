from django.shortcuts import render

# Create your views here.
def vijay(request):
    d={'name':'vijay'}
    return render(request,'for.html',context=d)
