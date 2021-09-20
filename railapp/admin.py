from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(WelcomeMsg)
admin.site.register(Day)
admin.site.register(Status)
admin.site.register(Start)
admin.site.register(End)
admin.site.register(Time)
admin.site.register(RailSchedule)