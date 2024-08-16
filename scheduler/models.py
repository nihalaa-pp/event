from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title



class Speaker(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(default='No bio provided')

    def __str__(self):
        return self.name


class Session(models.Model):
    event = models.ForeignKey(Event, related_name='sessions', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def clean(self):
        # Prevent time conflicts within the same event
        if self.start_time >= self.end_time:
            raise ValidationError('End time must be after start time')
        overlapping_sessions = Session.objects.filter(
            event=self.event,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(pk=self.pk)
        if overlapping_sessions.exists():
            raise ValidationError('This session conflicts with another session in the same event')
