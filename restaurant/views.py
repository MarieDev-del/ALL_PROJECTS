# from django.http import HttpResponse
from django.shortcuts import render

from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from .forms import BookingForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add code for the bookings() view



def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})



def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 
        
        
        
        
    
    

from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

def booking_view(request):
    form = BookingForm()
    reservations = []
    selected_date = request.GET.get('date')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"?date={form.cleaned_data['reservation_date']}")

    if selected_date:
        reservations = Booking.objects.filter(reservation_date=selected_date)

    context = {
        'form': form,
        'reservations': reservations,
        'selected_date': selected_date,
    }
    return render(request, 'reservations.html', context)

    
from django.http import JsonResponse
from .models import Booking

def bookings_list(request):
    date = request.GET.get('date') # Retrieve 'date' query parameter
    if date:
        bookings = Booking.objects.filter(reservation_date=date)
    else:
        bookings = Booking.objects.all()

    data = [
        {
            "model": "restaurant.booking",
            "pk": booking.id,
            "fields": {
                "first_name": booking.first_name,
                "reservation_date": booking.reservation_date.strftime('%Y-%m-%d'),
                "reservation_slot": booking.reservation_slot,
            }
        }
        for booking in bookings
    ]
    return JsonResponse(data, safe=False)




    
    
# from django.shortcuts import render, redirect
# from .forms import BookingForm
# from .models import Booking
# from django.http import JsonResponse

# # View for handling the booking form
# def bookings_form(request):
#     form = BookingForm()
#     booked_slots = None

#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             # Check if the time slot is already booked
#             reservation_date = form.cleaned_data['reservation_date']
#             reservation_slot = form.cleaned_data['reservation_slot']

#             # Prevent duplicate booking
#             if Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot).exists():
#                 form.add_error('reservation_slot', 'This time slot is already booked.')
#             else:
#                 form.save()
#                 return redirect('booking')  # Redirect to the same page or another success page

#     # Get already booked slots for a selected date (if provided in GET request)
#     if 'date' in request.GET:
#         date = request.GET['date']
#         booked_slots = Booking.objects.filter(reservation_date=date)

#     return render(request, 'restaurant/booking.html', {
#         'form': form,
#         'booked_slots': booked_slots,
#     })


# API view to return JSON data of bookings for a specific date
def bookings_api(request):
    date = request.GET.get('date', None)
    if date:
        bookings = Booking.objects.filter(reservation_date=date)
        data = [
            {
                "first_name": booking.first_name,
                "reservation_date": booking.reservation_date,
                "reservation_slot": booking.reservation_slot.strftime('%H:%M')
            }
            for booking in bookings
        ]
        return JsonResponse(data, safe=False)
    return JsonResponse({"error": "No date provided"}, status=400)

