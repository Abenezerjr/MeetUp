from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm


# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    context = {
        'meetups': meetups
    }
    return render(request, 'meetapps/index.html', context)


def meetupDetails(request, meetup_slug):
    try:
        selectedMeetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == "GET":
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)

                selectedMeetup.participants.add(participant)
                return redirect('confirm', meetup_slug=meetup_slug)

        context = {
            'meetup_found': True,
            "meetup": selectedMeetup,
            'form': registration_form,
        }
        return render(request, 'meetapps/meetup-details.html', context)
    except Exception as exc:
        return render(request, 'meetapps/meetup-details.html', {'meetup_found': False})


def confirm(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    context = {
        "meetup": meetup.organizer_email
    }
    return render(request, 'meetapps/meetup-success.html', context)
