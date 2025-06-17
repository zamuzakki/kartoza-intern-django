from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Staff

# Create your views here.
def index(request):
    staffs = Staff.objects.all().order_by('name')
    context = {
        'staff_list': staffs
    }
    return render(request, 'myapp/index.html', context)


def detail(request, staff_id):
    staff = get_object_or_404(Staff, pk=staff_id)
    context = {
        'staff': staff
    }
    return render(request, 'myapp/detail.html', context)


def create(request):
    return HttpResponse('You are looking at the create page.')