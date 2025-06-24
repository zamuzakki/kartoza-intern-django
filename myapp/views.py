from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .forms import StaffForm
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
    # GET
    if request.method == 'GET':
        form = StaffForm()
        context = {
            'form': form
        }
        return render(request, 'myapp/create.html', context)
    elif request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            staff = form.save()
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect(
                reverse('myapp:detail', args=[staff.id])
            )
    else:
        return HttpResponse('Invalid request')