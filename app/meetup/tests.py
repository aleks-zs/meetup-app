from django.test import TestCase, Client
from django.urls import reverse
from .models import Meetup, Location


# Create your tests here.

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('index')
        self.meetup_details = reverse('meetup-detail', args=['test-meetup'])
        self.meetup_details_confirm = reverse('confirm-registration', args=['test-meetup']) # noqa

        self.test_meetup = Meetup.objects.create(
            slug='test-meetup',
            date='2023-01-19',
            location=Location.objects.create(),
            image='test-image'
        )

    def test_index_GET(self):
        res = self.client.get(self.index)
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, "meetup/index.html")

    def test_meetup_details_GET(self):
        res = self.client.get(self.meetup_details)
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, "meetup/meetup-details.html")

    def test_meetup_details_register_POST(self):
        res = self.client.post(self.meetup_details, {
            "email": "test@email.com",
        }, follow=True)
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, "meetup/registration-success.html")
        self.assertEquals(self.test_meetup.participants.first().email, 'test@email.com') # noqa
