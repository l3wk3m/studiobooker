from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.contrib import messages
from .models import Studio, StudioBooking
from users.models import CustomUser, UserProfile

def studio_detail(request, pk):
    """ A view to show a studio's image and decsription before booking """
    
    studio = get_object_or_404(Studio, pk=studio_id)

    template = 'booking/studio_detail.html'

    return render(request, template, {'studio': studio})