from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the sendData index.")


def sendData(request):
    print("at sendData")
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'send_data.html')
