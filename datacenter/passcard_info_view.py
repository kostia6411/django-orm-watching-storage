from datacenter.models import Passcard, Visit
from django.shortcuts import render
from .models import is_visit_long, get_duration
from .storage_information_view import format_duration
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)

    user_visit = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in user_visit:

        duration = get_duration(visit)

        is_strange = is_visit_long(duration, minutes=60)

        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': format_duration(duration),
                'is_strange': is_strange
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
