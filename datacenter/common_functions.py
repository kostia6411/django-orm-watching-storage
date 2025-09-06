import django


def is_visit_long(spent_time, minutes=60):
    seconds_duration = 60
    spent_minutes = spent_time.seconds / seconds_duration
    return spent_minutes >= minutes


def get_duration(visit):
    if visit.leaved_at:
        spent_time = visit.leaved_at - visit.entered_at
    else:
        time = django.utils.timezone.localtime()
        spent_time = time - visit.entered_at
    return spent_time


def format_duration(duration):
    hour_seconds = 3600
    minute_seconds = 60
    hour_duration_remains = duration.seconds / hour_seconds
    hour_duration = duration.seconds // hour_seconds
    minute_duration = int(minute_seconds * (hour_duration_remains - hour_duration))
    return f'{hour_duration}ч {minute_duration}мин'