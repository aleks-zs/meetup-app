from django.shortcuts import render


# Create your views here.
def index(request):

    meetups = [
        {
         'title': 'First meetup',
         'location': 'Madrid',
         'slug': 'first-meetup'
         },
        {
         'title': 'Second meetup',
         'location': 'Rome',
         'slug': 'second-meetup'
         }
    ]
    return render(request, 'meetup/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_details(request, slug):
    selected_meetup = {
        'title': 'Meetup Title',
        'description': 'Meetup Description'
    }
    return render(request, 'meetup/meetup-details.html', {
        'selected_meetup': selected_meetup
    })
