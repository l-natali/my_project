from django.shortcuts import render, HttpResponse
from .models import Category, Dishes


def base(request):
    items = Category.objects.all()

    res = '<br>'.join(map(str, items))
    return HttpResponse('Hello from base page<br>' + res)

