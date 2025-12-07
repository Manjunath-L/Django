from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def dynamic_url(request, id, name):
    print(f"This is the value we got -> {id}")
    return render(request, "dy.html", context={"id": id, "name": name})
