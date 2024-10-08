from django.shortcuts import render

def aplic(request):
    return render(request, "index.html")
