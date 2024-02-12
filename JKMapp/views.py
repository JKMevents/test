from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mambers(request):
    return HttpResponse("Hello world!")


def Home(request):
    return render(
        request,
        "index.html",
        {}
    )
