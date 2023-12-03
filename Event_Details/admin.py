from django.contrib import admin
from .models import EventDetails
class EventDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'event_date', 'event_starttime', 'event_endtime', 'hospital', 'date_registered')
    search_fields = ('name', 'description', 'location', 'event_date', 'event_starttime', 'event_endtime', 'hospital', 'date_registered')
    list_filter = ('name', 'description', 'location', 'event_date', 'hospital')
    ordering = ('event_date','hospital', 'name')
admin.site.register(EventDetails, EventDetailsAdmin)

