from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("", views.calendar_list, name="calendar_list"),
    path("calendar/<int:calendar_id>/", views.calendar_detail, name="calendar_detail"),
    path("event/<int:event_id>/", views.event_detail, name="event_detail"),
]
