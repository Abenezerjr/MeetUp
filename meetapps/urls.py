from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='meetup'),  # domain.com/meetup
    path('<slug:meetup_slug>/', views.meetupDetails, name='details'),
    # domain.com/meetup/<dynamic-path-segment>
    path('<slug:meetup_slug>/sccess', views.confirm, name='confirm'),
]
