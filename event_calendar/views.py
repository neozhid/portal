from django.shortcuts import render, get_object_or_404
from .models import Calendar, Event


def calendar_list(request):
    calendars = Calendar.objects.all()

    return render(request, "calendar/calendar_list.html", {
        "calendars": calendars
    })


def calendar_detail(request, calendar_id):
    calendar = get_object_or_404(Calendar, id=calendar_id)
    events = calendar.events.all().order_by("start_date")

    return render(request, "calendar/calendar_detail.html", {
        "calendar": calendar,
        "events": events
    })


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    return render(request, "calendar_detail.html", {
        "event": event
    })