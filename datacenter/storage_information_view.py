from datacenter.models import Visit
from django.shortcuts import render
import django


def get_duration(visit):
    if visit.leaved_at:
        spent_time = visit.leaved_at - visit.entered_at
    else:
        time = django.utils.timezone.localtime()
        spent_time = time - visit.entered_at
    return spent_time


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

        duration = format_duration(duration)

        non_closed_visits.append(
            {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': duration,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
