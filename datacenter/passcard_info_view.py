from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .storage_information_view import get_duration, format_duration
from .models import is_visit_long


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits_user = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits_user:
        duration = get_duration(visit)

        is_strange = is_visit_long(duration)

        duration = format_duration(duration)

        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': is_strange,
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }
    return render(request, 'passcard_info.html', context)
