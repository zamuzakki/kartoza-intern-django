from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff

# Create your views here.
def index(request):
    staffs = Staff.objects.all().order_by('name')
    output = ', '.join([str(staff) for staff in staffs])
    return HttpResponse(output)


def detail(request, staff_id):
    return HttpResponse('You are looking at the detail page.')


def create(request):
    return HttpResponse('You are looking at the create page.')