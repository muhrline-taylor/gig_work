from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('doorDash', views.DoorDashLandingView.as_view(), name='door_dash'),
    path('doorDash/all', views.DoorDashAllView.as_view(), name='door_dash_all'),
    path('doorDash/day/<int:id>', views.DoorDashOneView.as_view(), name='door_dash_day'),
    path('doorDash/new', views.DoorDashCreateView.as_view(), name='door_dash_new'),
    path('doorDash/month/<slug:month>', views.DoorDashMonthView.as_view(), name='door_dash_month'),
    path('doorDash/weekday/<slug:weekday>', views.DoorDashWeekdayView.as_view(), name='door_dash_weekday'),
]