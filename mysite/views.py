from django.shortcuts import render,redirect
import csv

# Create your views here.

def home(request):
    context = {}
    return render(request,'mysite/home.html',context)

def AutoTheftStolen(request):
    return render(request,'mysite/Auto_Theft_Stolen.html')

def CasesPropertyStolen(request):
    return render(request,'mysite/Cases_Property_Stolen.html')

def TotalKidnapp(request):
    return render(request,'mysite/Total_Kidnapp.html')

def TotalMurder(request):
    return render(request,'mysite/Total_Murders.html')

def TotalRape(request):
    return render(request, 'mysite/Victims_of_Rape_Total.html')

def TotalCluster(request):
    return render(request, 'mysite/Total_CLUSTERS.html')