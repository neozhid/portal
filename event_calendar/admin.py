from django.contrib import admin
from .models import Calendar, Event


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name", "description")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "calendar",
        "start_date",
        "end_date",
        "location",
    )
    list_filter = ("calendar", "start_date")
    search_fields = ("title", "description", "location")
    ordering = ("start_date",)