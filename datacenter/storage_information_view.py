from datacenter.models import Visit
from django.shortcuts import render

from .models import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    for visitor in visits:
        duration = get_duration(visitor)
        formated_duration = format_duration(duration)
        is_strange = is_visit_long(visitor)
        non_closed_visits.append(
            {
                "who_entered": visitor.passcard,
                "entered_at": visitor.entered_at,
                "duration": formated_duration,
                "is_strange": is_strange,
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
