# from django.shortcuts import render, get_object_or_404
# from .models import Calendar, Event


# def calendar_list(request):
#     calendars = Calendar.objects.all()

#     return render(request, "calendar/calendar_list.html", {
#         "calendars": calendars
#     })


# def calendar_detail(request, calendar_id):
#     calendar = get_object_or_404(Calendar, id=calendar_id)
#     events = calendar.events.all().order_by("start_date")

#     return render(request, "calendar/calendar_detail.html", {
#         "calendar": calendar,
#         "events": events
#     })


# def event_detail(request, event_id):
#     event = get_object_or_404(Event, id=event_id)

#     return render(request, "calendar/calendar_detail.html", {"event": event})

from collections import defaultdict
from datetime import timedelta

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Calendar, Event


def calendar_detail(request, calendar_id):
    calendar = get_object_or_404(Calendar, id=calendar_id)
    events = calendar.events.all().order_by("start_date")

    grouped_events = defaultdict(list)

    for event in events:
        start = timezone.localtime(event.start_date).date()
        end = timezone.localtime(event.end_date).date()

        current_date = start
        while current_date <= end:
            grouped_events[current_date].append(event)
            current_date += timedelta(days=1)

    dates = sorted(grouped_events.items())

    return render(request, "calendar/calendar_detail.html", {
        "calendar": calendar,
        "events": events,
        "dates": dates,
    })


def calendar_list(request):
    calendars = Calendar.objects.all()

    return render(request, "calendar/calendar_list.html", {
        "calendars": calendars
    })


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    return render(request, "calendar/event_detail.html", {
        "event": event
    })
