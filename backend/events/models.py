from django.db import models
from django.contrib.auth.models import User



class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField() 
    creator = models.ForeignKey(User, related_name='created_events', on_delete=models.CASCADE)
    place = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='events', blank=True, null=True)
    participantsCount = models.IntegerField(default=0)
    participantsMax = models.IntegerField(default=0)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return self.name




class Participant(models.Model):
    event = models.ForeignKey(Event, related_name='participants', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='joined_events', on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"
