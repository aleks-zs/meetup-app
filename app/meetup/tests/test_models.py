from django.test import TestCase
from meetup.models import Location, Participant, Meetup


class ModelsTests(TestCase):

    def test_create_location(self):
        location = Location.objects.create(name='name', address='address')
        self.assertTrue(location.name in str(location))
        self.assertTrue(location.address in str(location))

    def test_create_participant(self):
        participant = Participant.objects.create(email='participant@email.com')
        self.assertEqual(str(participant), participant.email)

    def test_create_meetup(self):
        slug = 'slug'
        date = '2023-01-25'
        location = Location.objects.create()
        image = 'image'

        meetup = Meetup.objects.create(
            title='title',
            slug=slug,
            date=date,
            location=location,
            image=image
        )

        self.assertEqual(str(meetup), meetup.title)
        self.assertEqual(meetup.slug, slug)
        self.assertEqual(meetup.date, date)
        self.assertEqual(meetup.location, location)
        self.assertEqual(meetup.image, image)
