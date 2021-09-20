from django.db import models

# Create your models here.
class WelcomeMsg(models.Model):
    title = models.CharField(max_length = 250)
    tagline = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.title
    
class Day(models.Model):
    journey_day = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.journey_day
    
class Status(models.Model):
    status = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.status
    
class Start(models.Model):
    start = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.start

class End(models.Model):
    end = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.end

class Time(models.Model):
    journey_time = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.journey_time
    
    
class RailSchedule(models.Model):
    tt_name = models.CharField(max_length = 250)
    date = models.CharField(max_length = 250)
    start_point = models.ForeignKey(Start, on_delete = models.CASCADE)
    end_point = models.ForeignKey(End, on_delete = models.CASCADE)
    day = models.ForeignKey(Day, on_delete = models.CASCADE)
    time = models.ForeignKey(Time, on_delete = models.CASCADE)
    journey_status = models.ForeignKey(Status, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.tt_name
    
     
    