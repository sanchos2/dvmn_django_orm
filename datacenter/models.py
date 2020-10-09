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


def get_duration(visit):
    entered_at = timezone.localtime(visit.entered_at)
    if not visit.leaved_at:
        leaved_at = timezone.localtime()
    else:
        leaved_at = timezone.localtime(visit.leaved_at)
    delta = leaved_at - entered_at
    return delta


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    duration_minutes = duration.total_seconds() // 60
    if duration_minutes >= minutes:
        return True
    return False


def format_duration(duration):
    seconds = duration.total_seconds()
    hour = seconds // 3600
    min = seconds % 3600 // 60
    sec = seconds % 3600 % 60
    return f'{hour:.0f}:{min:.0f}:{sec:.0f}'
