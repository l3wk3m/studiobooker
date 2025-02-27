import uuid
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from .models import Studio, StudioBooking
from users.models import CustomUser, UserProfile

# Create your views here.

def index(request):
    # Returns the index.html page

    artists = UserProfile.objects.all()

    context = {
        'artists': artists,
    }

    return render(request, 'booking/index.html', context)
    

def studios(request):
    template = 'booking/studios.html'
    context = {
        'studios': studios,
    }
    return render(request, template, context)


def booker(request):

    studios = Studio.objects.all()

    template = 'booking/booking.html'
    context = {
        'studios': studios,
        'booker': booker,
    }
    return render(request, template, context)

def studio_detail(request, studio_id):
    """ A view to show a studio's image and decsription before booking """
    
    studio = get_object_or_404(Studio, pk=studio_id)

    # First I'll call a function to check which days are weekdays over the next 14 days and place them in an array called weekdays
    weekdays = validWeekday(15)

    # Check array of weekdays to only show the days that aren't fully booked:
    validateWeekdays = isWeekdayValid(weekdays)
    
    print(studio)
    print(studio_id)

    # Next I'll make sure the user selects a date before continuing
    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')
        request.session['booking_date'] = booking_date
        request.session['studio_id'] = studio_id
        
        # Session data is stored and we're sent to the page where we'll choose our studio timeslot
        return redirect('booking_submit', studio.studio_id)
    
    template = 'booking/studio_detail.html'

    # In the context we'll return our valid weekdays from the function we called at the top of this one
    context = {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'studio': studio,
            'studio_id': studio_id
        }

    return render(request, template, context)


#   THE BELOW VIEW WILL SEND CHOSEN INFO ABOUT THE 'ALREADY SELECTED STUDIO' INTO SESSION ID ON THE STUDIO_DETAIL PAGE
# A view to submit your preferred time after selecting your studio
    # First I'll call a function to check which days are weekdays over the next 14 days and place them in an array called weekdays

# A view for a user to confirm what time slot they want to book for
# This view will only allow users to select a timeslot that is not already booked
def booking_submit(request, studio_id):
    
    artist = UserProfile.objects.get(username=request.user)
    times = [
        "9am to 12pm",
        "12pm to 3pm",
        "3pm to 6pm"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=14)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    # Retrieve stored session data
    if 'booking_date' in request.session:
        studio_id = request.session.get('studio_id')
        booking_date = request.session.get('booking_date')
        print(f'successfully stored the booking date and studio id, its {studio_id} on {booking_date}! - redirecting!')
    else:
        print('session data not found!')

#    booking_date = request.POST.get('booking_date')

#    studio_id = request.session.get('studio_id')
#    booking_date = request.session.get('booking_date')
#    studio = request.session.get('studio_id')

    # Call a function that only show users timeslots that haven't already been booked
    # This will iterate through the StudioBooking model to see if there is an entry in time for each time_slot using checkTime
    # If there is, that timeslot won't be displayed
    # Only show the time of the day that has not been selected before:

    #   C L E A N   U P   ! ! !
    
    hour = checkTime(times, booking_date)
    if request.method == 'POST':
        booking_time = request.POST.get("booking_time")
        date = dayToWeekday(booking_date)
        

        if booking_date <= maxDate and booking_date >= minDate:
            if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday':
                if StudioBooking.objects.filter(booking_date=booking_date).count() < 4:
                    if StudioBooking.objects.filter(booking_date=booking_date, booking_time=booking_time).count() < 1:
                        StudioBookingForm = StudioBooking.objects.get_or_create(
                            artist = artist,
                            studio_id = studio_id,
                            booking_date = booking_date,
                            booking_time = booking_time
                        )
                        messages.success(request, "Booking Saved!")
                        request.session['booking_date'] = booking_date
                        request.session['booking_time'] = booking_time
                        request.session['studio_id'] = studio_id
                        return redirect('booking_success')
                    else:
                        messages.success(request, "The Selected Time Has Been Reserved Before!")
                else:
                    messages.success(request, "The Selected Day Is Full!")
            else:
                messages.success(request, "The Selected Date Is Incorrect")
        else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")



    # User is given a confirmation message of their studio, date and timeslot

    template = 'booking/booking_submit.html'

    context = {
        'times': hour,
        'studio_id': studio_id
    }

    return render(request, template, context)

def booking_success(request):

    artist = UserProfile.objects.get(username=request.user)
    studio_id = request.session.get('studio_id')
    booking_date = request.session.get('booking_date')
    booking_time = request.session.get('booking_time')

    template = 'booking/booking_success.html'
    
    context = {
        'studio_id': studio_id,
        'booking_date': booking_date,
        'booking_time': booking_time,
        'artist': artist
    }

    return render(request, template, context)

# A view for users to view their bookings
def user_panel(request):
    artist = UserProfile.objects.get(username=request.user)
    bookings = StudioBooking.objects.filter(artist=artist).order_by('booking_date', 'booking_time')
    return render(request, 'booking/user_panel.html', {
        'artist': artist,
        'bookings': bookings,
    })

# A view for users to edit their bookings (will be similar to the booking view)
def user_update(request, booking_id):
    artist = UserProfile.objects.get(username=request.user)
    booking = StudioBooking.objects.get(pk=booking_id)
    userdatepicked = booking.booking_date
    studio_id = request.session.get('studio_id')
    booking_date = booking.booking_date
    #Copy  booking:
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    #24h if statement in template:
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    #Calling 'validWeekday' Function to Loop days you want in the next 14 days:
    weekdays = validWeekday(15)

    #Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)
    

    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')

        #Store day and service in django session:
        request.session['booking_date'] = booking_date
        request.session['studio_id'] = studio_id

        return redirect('user_update_submit', booking_id)


    return render(request, 'booking/user_update.html', {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'delta24': delta24,
            'booking_id': booking_id,
            'booking_date': booking_date,
        })


def user_update_submit(request, booking_id):
    artist = UserProfile.objects.get(username=request.user)
    times = [
        "9am to 12pm",
        "12pm to 3pm",
        "3pm to 6pm"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    booking_date = request.session.get('booking_date')
    studio_id = request.session.get('studio_id')
    
    #Only show the time of the day that has not been selected before and the time he is editing:
    hour = checkEditTime(times, booking_date, booking_id)
    booking = StudioBooking.objects.get(booking_id=booking_id)
    userSelectedTime = booking.booking_time
    
    if request.method == 'POST':
        booking_time = request.POST.get("booking_time")
        date = dayToWeekday(booking_date)

        if booking_date <= maxDate and booking_date >= minDate:
            if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday':
                if StudioBooking.objects.filter(booking_date=booking_date).count() < 4:
                    if StudioBooking.objects.filter(booking_date=booking_date, booking_time=booking_time).count() < 1 or userSelectedTime == time:
                        StudioBookingForm = StudioBooking.objects.filter(booking_id=booking_id).update(
                            artist = artist,
                            studio_id = studio_id,
                            booking_date = booking_date,
                            booking_time = booking_time,
                        ) 
                        messages.success(request, "Booking Edited!")
                        request.session['booking_date'] = booking_date
                        request.session['booking_time'] = booking_time
                        request.session['studio_id'] = studio_id
                        return redirect('update_success')
                    else:
                        messages.success(request, "The Selected Time Has Been Reserved Before!")
                else:
                    messages.success(request, "The Selected Day Is Full!")
            else:
                messages.success(request, "The Selected Date Is Incorrect")
        else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        return redirect('userPanel')


    return render(request, 'booking/user_update_submit.html', {
        'times':hour,
        'booking_id': booking_id,
    })

def update_success(request):

    artist = UserProfile.objects.get(username=request.user)
    studio_id = request.session.get('studio_id')
    booking_date = request.session.get('booking_date')
    booking_time = request.session.get('booking_time')

    template = 'booking/update_success.html'
    
    context = {
        'studio_id': studio_id,
        'booking_date': booking_date,
        'booking_time': booking_time,
        'artist': artist
    }

    return render(request, template, context)

# Views for superusers to view and edit bookings
def staff_panel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=14)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Bookings 14 days from today
    items = StudioBooking.objects.filter(booking_date__range=[minDate, maxDate]).order_by('booking_date', 'booking_time')

    return render(request, 'booking/staff_panel.html', {
        'items':items,
    })

# A function to take in a variable that's a datetime object and translate it to it's full weekday name for use in other functions
def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

# A function to check for valid weekdays in a range of 14 days
def validWeekday(days):
    #Loop days you want in the next 14 days:
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A') # %A is strftime tag for full weekday name
        if y == 'Monday' or y == 'Tuesday' or y == 'Wednesday' or y == 'Thursday' or y == 'Friday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays

# A function that checks whether a weekday is fully booked. 'x' here is the array of weekdays we found with the validWeekday function
def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if StudioBooking.objects.filter(booking_date=j).count() < 3:
            validateWeekdays.append(j)
    return validateWeekdays

# A function that returns an array of only available timeslots on a given day
def checkTime(times, booking_date):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if StudioBooking.objects.filter(booking_date=booking_date, booking_time=k).count() < 1:
            x.append(k)
    return x

# A function that returns an array of only available timeslots on a given day when editing a booking
def checkEditTime(times, booking_date, booking_id):
    #Only show the time of the day that has not been selected before:
    x = []
    booking = StudioBooking.objects.get(booking_id=booking_id)
    time = booking.booking_time
    for k in times:
        if StudioBooking.objects.filter(booking_date=booking_date, booking_time=k).count() < 1 or time == k:
            x.append(k)
    return x