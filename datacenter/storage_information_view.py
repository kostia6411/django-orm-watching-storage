from datacenter.models import Visit
from django.shortcuts import render
from .models import get_duration


def format_duration(duration):
    hour_seconds = 3600
    minute_seconds = 60
    hour_duration_remains = duration.total_seconds() / hour_seconds
    hour_duration = int(duration.total_seconds() // hour_seconds)
    minute_duration = int(minute_seconds * (hour_duration_remains - hour_duration))
    return f'{hour_duration}ч {minute_duration}мин'


def storage_information_view(request):

    unfinished_visit = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []

    for visit in unfinished_visit:

        duration = get_duration(visit)

        non_closed_visits.append({
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
