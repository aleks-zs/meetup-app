from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>', views.meetup_details, name='meetup-detail'),
    path('<slug:slug>/success', views.confirm_registration, name='confirm-registration'),  # noqa
]
