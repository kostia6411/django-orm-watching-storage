from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from .common_functions import get_duration, format_duration, is_visit_long



def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
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
