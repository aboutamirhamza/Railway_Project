from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    home_msg = WelcomeMsg.objects.all()
    home_con = {'home_message':home_msg}
    return render(request, 'home.html',home_con)

def railsche(request):
    rail_sch = RailSchedule.objects.all()
    rail_con = {'rail_schedule':rail_sch}
    return render(request, 'rail_schedule.html',rail_con)