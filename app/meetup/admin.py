from django.contrib import admin # noqa
from .models import Meetup, Location, Participant


# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_filter = ('name',)


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('email',)


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Location, LocationAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Meetup, MeetupAdmin)
