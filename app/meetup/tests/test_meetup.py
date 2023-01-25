from django.test import TestCase, Client
from django.urls import reverse
from meetup.models import Meetup, Location


# Create your tests here.

def create_meetup(**params):
    return Meetup.objects.create(**params)


class ViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('index')
        self.meetup_details = reverse('meetup-detail', args=['test-meetup'])
        self.meetup_details_confirm = reverse('confirm-registration', args=['test-meetup'])  # noqa

    def test_get_index(self):
        res = self.client.get(self.index)
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, "meetup/index.html")

    def test_get_meetup_details(self):
        res = self.client.get(self.meetup_details)
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, "meetup/meetup-details.html")

    def test_post_meetup_details_registration(self):
        test_meetup = create_meetup(
            slug='test-meetup',
            date='2023-01-19',
            location=Location.objects.create(),
            image='test-image'
        )
        res = self.client.post(self.meetup_details, {"email": "test@email.com", }, follow=True) # noqa
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, "meetup/registration-success.html")
        self.assertEquals(test_meetup.participants.first().email, 'test@email.com')  # noqa
