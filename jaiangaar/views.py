from django.http import HttpResponse

from django.shortcuts import render




def cham(request):
    return render(request,"cham.html")


