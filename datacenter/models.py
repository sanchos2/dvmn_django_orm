from datetime import datetime
from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'

    class Meta:
        ordering = ('owner_name',)


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(self):
        entered_at = timezone.localtime(self.entered_at)
        if not self.leaved_at:
            leaved_at = timezone.localtime()
        else:
            leaved_at = timezone.localtime(self.leaved_at)
        delta = leaved_at - entered_at
        total_seconds = delta.total_seconds()
        return total_seconds


def is_visit_long(visit, minutes=60):
    duration = visit.get_duration()
    duration_minutes = duration // 60
    return duration_minutes >= minutes


def format_duration(duration):
    hour = str(int(duration // 3600))
    minutes = str(int(duration % 3600 // 60))
    seconds = str(int(duration % 3600 % 60))
    return f'{hour.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}'
