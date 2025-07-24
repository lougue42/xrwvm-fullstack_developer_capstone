# Uncomment the required imports before adding the code

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib import messages
# from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel
from .populate import initiate

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create a `login_user` view to handle sign in request
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"})
        else:
            return JsonResponse({"status": "Failed"})

# Create a `get_cars` view to load/populate cars
def get_cars(request):
    count = CarMake.objects.count()
    if count == 0:
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = [{"CarModel": c.name, "CarMake": c.car_make.name} for c in car_models]
    return JsonResponse({"CarModels": cars})

# Create a `logout_user` view to handle sign out request
# def logout_user(request):
#     ...

# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
#     ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
# def get_dealerships(request):
#     ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request, dealer_id):
#     ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
#     ...

# Create an `add_review` view to submit a review
# def add_review(request):
#     ...
