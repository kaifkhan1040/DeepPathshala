from django.shortcuts import render
from .forms import contactform
from student.models import Activity
from .models import *
from student.models import *
from .models import Subscribe
from django.contrib import messages


# Create your views here.
def home(request):
    course = Course.objects.all()[:6]
    teacherlen=Teacher.objects.all().count()
    courselen=Course.objects.all().count()
    studentlen=User.objects.all().count()-teacherlen
    return render(request, 'home/index.html', {'course': course,'courselen':courselen,'teacherlen':teacherlen,'studentlen':studentlen})


def aboutus(request):
    return render(request, 'home/about.html')


def contactus(request):
    form = contactform()
    if request.method == 'POST':
        details = contactform(request.POST)
        print(details.errors)
        if details.is_valid():
            details.save()
            print('saved')

    return render(request, 'home/contact.html', {'form': form})


def subscribe(request):
    print(request.method)
    if request.method == "POST":
        num = request.POST.get('newsletter')
        if len(num) == 10:
            res=Subscribe(number=num)
            res.save()
            messages.success(request, 'Subscribe successful')
        else:
            messages.error(request, 'Please Enter The Valid Number')
    return render(request, 'home/index.html')
