from datacenter.models import Visit
from django.shortcuts import render
from .models import get_duration


def format_duration(duration):
    hour_duration_remains = duration.seconds / 3600
    hour_duration = duration.seconds // 3600
    minute_duration = int(60 * (hour_duration_remains - hour_duration))
    return f'{hour_duration}ч {minute_duration}мин'


def storage_information_view(request):

    visit_all = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []

    for visit in visit_all:

        duration = get_duration(visit)

        non_closed_visits.append({
            'who_entered': f'{visit.passcard}',
            'entered_at': f'{visit.entered_at}',
            'duration': f'{format_duration(duration)}',
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
