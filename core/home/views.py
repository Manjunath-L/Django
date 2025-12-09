from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View
import random

# Create your views here.


def index(request):
    lucky_num = random.randint(100, 999)
    vegatables = ["Tomoto", "Potato", "Chilly"]
    person = 19
    context = {"lucky_num": lucky_num, "Vegatbles": vegatables, "person": person}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def dynamic_url(request, id, name):
    print(f"This is the value we got -> {id}")
    return render(request, "dy.html", context={"id": id, "name": name})


def project(request):
    lucky_num = random.randint(1, 10)
    context = {"lucky_num": lucky_num}
    return render(request, "project.html", context)
