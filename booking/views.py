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

    # Get the studio id
    # if request.method == 'GET':

    # The rationale here is that HttpRequest.path() takes everything AFTER the domain name and returns it as an array of strings
    # The studio id will be the second item in that array after 'bookings'
    # Its then converted into an Int and stored in session data
#    studio_id = request.GET.items()


    #request.session['studio_id'] = studio

    
    print(studio)
    print(studio_id)

    # Next I'll make sure the user selects a date before continuing
    if request.method == 'POST':
        date = request.POST.get('booking_date')
    #    studio = request.POST.get('studio_id')

        request.session['booking_date'] = date
    #    request.session['studio_id'] = studio
        context = {
                'studio_id': studio_id,
                'studio': studio
            }
        # Session data is stored and we're sent to the page where we'll choose our studio timeslot
        return redirect('booking_time', context)

    
    template = 'booking/studio_detail.html'

    # In the context we'll return our valid weekdays from the function we called at the top of this one
    context = {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'studio': studio,
            'studio_id': studio_id
        }

    return render(request, template, context)


def blog(request):

# Will retrieve all posts from the blog model when its set up
    # post_list = Posts.objects.all() 

    template = 'booking/blog.html'
    context = {
        'blog': blog,
    }
    return render(request, template, context)

def studios(request):
    template = 'booking/studios.html'
    context = {
        'studios': studios,
    }
    return render(request, template, context)

#   THE BELOW VIEW WILL SEND CHOSEN INFO ABOUT THE 'ALREADY SELECTED STUDIO' INTO SESSION ID ON THE STUDIO_DETAIL PAGE
# A view to submit your preferred time after selecting your studio
def booking(request):
    # First I'll call a function to check which days are weekdays over the next 14 days and place them in an array called weekdays
    weekdays = validWeekday(15)

    # Check array of weekdays to only show the days that aren't fully booked:
    validateWeekdays = isWeekdayValid(weekdays)

    # Get the studio id
    # if request.method == 'GET':

    # The rationale here is that HttpRequest.path() takes everything AFTER the domain name and returns it as an array of strings
    # The studio id will be the second item in that array after 'bookings'
    # Its then converted into an Int and stored in session data
    studio = int(HttpRequest.path.split("/", )[1])

    print(studio)

    request.session['studio_id'] = studio

    # Next I'll make sure the user selects a date before continuing
    if request.method == 'POST':
        date = request.POST.get('booking_date')
    #    studio = request.POST.get('studio_id')

        request.session['booking_date'] = date
    #    request.session['studio_id'] = studio

        # Session data is stored and we're sent to the page where we'll choose our studio timeslot
        return redirect('booking_submit')

    template = 'booking.html'

    # In the context we'll return our valid weekdays from the function we called at the top of this one
    context = {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
        }

    return render(request, template, context)

# A view for a user to confirm what time slot they want to book for
# This view will only allow users to select a timeslot that is not already booked
def booking_time(request, studio_id):
    studio_id = request.session.get('studio_id')
    artist = request.user
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
    date = request.session.get('booking_date')
    studio = request.session.get('studio_id')

    # Call a function that only show users timeslots that haven't already been booked
    # This will iterate through the StudioBooking model to see if there is an entry in time for each time_slot using checkTime
    # If there is, that timeslot won't be displayed
    # Only show the time of the day that has not been selected before:

    #   C L E A N   U P   ! ! !
    
    hour = checkTime(times, date)
    if request.method == 'POST':
        time = request.POST.get("booking_time")
        date = dayToWeekday(day)

        if date <= maxDate and date >= minDate:
            if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday':
                if StudioBooking.objects.filter(day=booking_date).count() < 4:
                    if StudioBooking.objects.filter(day=booking_date, time=booking_time).count() < 1:
                        StudioBookingForm = StudioBooking.objects.get_or_create(
                            artist = artist,
                            studio_id = studio_id,
                            booking_date = booking_date,
                            booking_time = booking_time,
                        )
                        messages.success(request, "Booking Saved!")
                        return redirect('index')
                    else:
                        messages.success(request, "The Selected Time Has Been Reserved Before!")
                else:
                    messages.success(request, "The Selected Day Is Full!")
            else:
                messages.success(request, "The Selected Date Is Incorrect")
        else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")



    # User is given a confirmation message of their studio, date and timeslot

    template = 'booking_time.html'

    context = {
        'times':hour,
    }

    return render(request, template, context)

# A view for users to view their bookings
def userPanel(request):
    artist = request.artist
    bookings = StudioBooking.objects.filter(artist=artist).order_by('booking_date', 'booking_time')
    return render(request, 'userPanel.html', {
        'artist':artist,
        'bookings':bookings,
    })

# A view for users to edit their bookings (will be similar to the booking view)
def userUpdate(request, id):
    booking = StudioBooking.objects.get(pk=id)
    userdatepicked = booking.booking_date
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
        service = request.POST.get('studio_id')
        day = request.POST.get('booking_date')

        #Store day and service in django session:
        request.session['booking_date'] = booking_date
        request.session['studio_id'] = studio_id

        return redirect('userUpdateSubmit', id=id)


    return render(request, 'userUpdate.html', {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'delta24': delta24,
            'id': id,
        })


def userUpdateSubmit(request, id):
    artist = request.artist
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

    date = request.session.get('booking_date')
    studio = request.session.get('studio_id')
    
    #Only show the time of the day that has not been selected before and the time he is editing:
    hour = checkEditTime(times, day, id)
    booking = StudioBooking.objects.get(pk=id)
    userSelectedTime = booking.booking_time
    
    if request.method == 'POST':
        time = request.POST.get("booking_time")
        date = dayToWeekday(day)

        if day <= maxDate and day >= minDate:
            if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday':
                if StudioBooking.objects.filter(day=booking_date).count() < 4:
                    if StudioBooking.objects.filter(day=booking_date, time=booking_time).count() < 1 or userSelectedTime == time:
                        StudioBookingForm = StudioBooking.objects.filter(pk=id).update(
                            artist = artist,
                            studio_id = studio_id,
                            booking_date = booking_date,
                            booking_time = booking_time,
                        ) 
                        messages.success(request, "Booking Edited!")
                        return redirect('index')
                    else:
                        messages.success(request, "The Selected Time Has Been Reserved Before!")
                else:
                    messages.success(request, "The Selected Day Is Full!")
            else:
                messages.success(request, "The Selected Date Is Incorrect")
        else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        return redirect('userPanel')


    return render(request, 'userUpdateSubmit.html', {
        'times':hour,
        'id': id,
    })

# Views for superusers to view and edit bookings
def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=14)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Bookings 14 days from today
    items = StudioBooking.objects.filter(booking_date__range=[minDate, maxDate]).order_by('booking_date', 'booking_time')

    return render(request, 'staffPanel.html', {
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
def checkTime(times, day):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if StudioBooking.objects.filter(booking_date=booking_date, booking_time=k).count() < 1:
            x.append(k)
    return x

# A function that returns an array of only available timeslots on a given day when editing a booking
def checkEditTime(times, day, id):
    #Only show the time of the day that has not been selected before:
    x = []
    booking = StudioBooking.objects.get(pk=id)
    time = booking.booking_time
    for k in times:
        if StudioBooking.objects.filter(booking_date=booking_date, booking_time=k).count() < 1 or time == k:
            x.append(k)
    return x