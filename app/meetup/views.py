from django.shortcuts import render
from .models import Meetup


# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetup/index.html', {
        'meetups': meetups
    })


def meetup_details(request, slug):
    try:
        meetup = Meetup.objects.get(slug=slug)

        return render(request, 'meetup/meetup-details.html', {
            'meetup_found': True,
            'selected_meetup': meetup
        })
    except Exception:
        return render(request, 'meetup/meetup-details.html', {
            'meetup_found': False
        })
