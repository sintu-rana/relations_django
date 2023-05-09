from django.shortcuts import render

# Create your views here.

def view_first(request):
    resp=render(request,'app/hello.html')
    return resp