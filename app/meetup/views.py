from django.shortcuts import render, redirect
from .models import Meetup, Participant
from .forms import RegistrationForm


# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetup/index.html', {
        'meetups': meetups
    })


def meetup_details(request, slug):
    try:
        meetup = Meetup.objects.get(slug=slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email) # noqa
                meetup.participants.add(participant)
                return redirect('confirm-registration', slug=slug)

        return render(request, 'meetup/meetup-details.html', {
            'meetup_found': True,
            'selected_meetup': meetup,
            'form': registration_form
        })
    except Exception:
        return render(request, 'meetup/meetup-details.html', {
            'meetup_found': False
        })


def confirm_registration(request, slug):
    meetup = Meetup.objects.get(slug=slug)
    return render(request, 'meetup/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })
