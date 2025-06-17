from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('You are looking at the index page.')


def detail(request, staff_id):
    return HttpResponse('You are looking at the detail page.')


def create(request):
    return HttpResponse('You are looking at the create page.')