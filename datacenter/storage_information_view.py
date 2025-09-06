from datacenter.models import Visit
from django.shortcuts import render
from .common_functions import get_duration, format_duration

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
