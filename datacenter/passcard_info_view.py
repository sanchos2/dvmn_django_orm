from django.shortcuts import Http404, render

from .models import Passcard, Visit
from .models import format_duration


def passcard_info_view(request, passcode):
    try:
        passcard = Passcard.objects.get(passcode=passcode)
    except Passcard.DoesNotExist:
        raise Http404('Passcode not found')

    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        duration = visit.get_duration()
        formated_duration = format_duration(duration)
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': formated_duration,
                'is_strange': visit.is_visit_long(),
            }
        )
    context = {
        "passcard": passcard.owner_name,
        "this_passcard_visits": this_passcard_visits,
    }
    return render(request, 'passcard_info.html', context)
