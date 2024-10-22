from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.contrib import messages
from .models import Studio, StudioBooking
from users.models import CustomUser, UserProfile

# Create your views here.

def index(request):
    # Returns the index.html page
    return render(request, 'booking/index.html')

def booker(request):
    template = 'booking/booking.html'
    context = {
        'booker': booker,
    }
    return render(request, template, context)

def blog(request):
    template = 'booking/blog.html'
    context = {
        'blog': blog,
    }
    return render(request, template, context)

# A view to submit your preferred time after selecting your studio
def booking(request):
    # First I'll call a function to check which days are weekdays over the next 14 days and place them in an array called weekdays
    weekdays = validWeekday(15)

    # Check array of weekdays to only show the days that aren't fully booked:
    validateWeekdays = isWeekdayValid(weekdays)

    # Next I'll make sure the user selects a date before continuing
    if request.method == 'POST':
        date = request.POST.get('booking_date')
        studio = request.POST.get('studio_id')

        request.session['booking_date'] = date
        request.session['studio_id'] = studio

        # Session data is stored and we're sent to the page where we'll choose our studio timeslot
        return redirect('booking_submit')

    template = 'booking.html'

    # In the context we'll return our valid weekdays from the function we called at the top of this one
    context = {}

    return render(request, template, context)

# A view for a user to confirm what time slot they want to book for
# This view will only allow users to select a timeslot that is not already booked
def booking_submit(request):
    user = request.user
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

    # Retrieve stored session data
    date = request.session.get('booking_date')
    studio = request.session.get('studio_id')

    # Call a function that only show users timeslots that haven't already been booked
    # This will iterate through the StudioBooking model to see if there is an entry in time for each time_slot using checkTime
    # If there is, that timeslot won't be displayed
    # Only show the time of the day that has not been selected before:

    #   C L E A N   U P   ! ! !
    
    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Tuesday' or date == 'Wednesday' or date == 'Thursday' or date == 'Friday':
                    if StudioBooking.objects.filter(day=booking_date).count() < 11:
                        if StudioBooking.objects.filter(day=booking_date, time=booking_time).count() < 1:
                            StudioBookingForm = StudioBooking.objects.get_or_create(
                                user = user,
                                service = service,
                                day = day,
                                time = time,
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
        else:
            messages.success(request, "Please Select A Service!")


    return render(request, 'bookingSubmit.html', {
        'times':hour,
    })

    # User is given a confirmation message of their studio, date and timeslot

    template = ''

    context = {}

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
    appointment = Appointment.objects.get(pk=id)
    userdatepicked = appointment.day
    #Copy  booking:
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    #24h if statement in template:
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    #Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(22)

    #Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)
    

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')

        #Store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service

        return redirect('userUpdateSubmit', id=id)


    return render(request, 'userUpdate.html', {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'delta24': delta24,
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