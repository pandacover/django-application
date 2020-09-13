from django.shortcuts import render
from .models import Staff
# Create your views here.
def support(request):
    return render(request, './support.html')

def staff(request):
    staffs = Staff.objects.all()
    return render(request, './staff.html', {'staffs':staffs})

