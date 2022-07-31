from django.shortcuts import render, HttpResponse

# Create your views here.


def customer_general(request):
    return HttpResponse('Hello from customer page')


def customer(request, number):
    return HttpResponse(f'Hello from customer number {number}')


def bookatable(request):
    pass
