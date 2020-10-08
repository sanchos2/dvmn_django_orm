from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .models import is_visit_long, get_duration, format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        duration = get_duration(visit)
        formated_duration = format_duration(duration)
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': formated_duration,
                'is_strange': is_visit_long(visit),
            }
        )
    context = {
        "passcard": passcard.owner_name,
        "this_passcard_visits": this_passcard_visits,
    }
    return render(request, 'passcard_info.html', context)
