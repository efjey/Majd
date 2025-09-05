from django.shortcuts import render, HttpResponse

def helloAdmin(request):
    return render(request, 'index.htm')