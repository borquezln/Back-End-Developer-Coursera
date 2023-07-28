from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Little Lemon!")

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu")

def book(request):
    return HttpResponse("Make a booking")

def drinks(request, drink_name):
    drink = {
        "mocha" : "type of coffee",
        "tea" : "type of beverage",
        "lemonade" : "type of refreshment"
    }
    choice_of_drink = drink[drink_name]

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)