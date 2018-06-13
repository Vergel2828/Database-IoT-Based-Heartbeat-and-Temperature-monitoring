from datetime import datetime
from pytz import utc
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View

from rest_framework import generics
from rest_framework.fields import empty
from rest_framework.views import APIView
from rest_framework.response import Response

from HealthMonitoring.models import Profile, HeartRateData, TemperatureData 
from HealthMonitoring.forms import (
                                    LoginForm,
                                    RegistrationForm,
                                    HeartRateDataForm,
                                    TemperatureDataForm
                                    )
from HealthMonitoring.serializers import ShowProfileSerializer


def login_user(request, *args, **kwargs):
    errors = []
    if request.user.is_authenticated():
        return redirect("HealthMonitoring:home")
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("HealthMonitoring:home")
        else:
            errors.append("Your username or password is incorrect.")
    else:
        form = LoginForm()

    return render(request, "Login.html", {'form': form, 'errors':errors})


class Statistics(View):

    def get(self, request):
        errors = []
        if 'dateStart' in request.GET and 'dateEnd' in request.GET:
            dateStart = request.GET['dateStart']
            dateEnd = request.GET['dateEnd']
            if not dateStart or not dateEnd:
                errors.append("Please submit a start and end date to graph.")
            else:
                date_start_object = datetime.strptime(dateStart, '%m/%d/%Y %I:%M %p')
                aware_date_start = utc.localize(date_start_object)
                date_end_object = datetime.strptime(dateEnd, '%m/%d/%Y %I:%M %p')
                aware_date_end = utc.localize(date_end_object)
                if date_start_object > date_end_object:
                    errors.append("Start date is greater than end date.")
                elif date_start_object == date_end_object:
                    errors.append("Start date is equal to end date.")
                else:
                    heart_rate_data_query = HeartRateDataForm().query(aware_date_start, aware_date_end, request.user)
                    temperature_data_query = TemperatureDataForm().query(aware_date_start, aware_date_end, request.user)
                    text = "heart rate reading result"
                    if len(heart_rate_data_query) <= 30 and len(temperature_data_query) <= 30:
                        return render(
                            request,
                            "statistics.html",
                            {'user': request.user,
                            'heart_rate_data_query': heart_rate_data_query,
                            'temperature_data_query': temperature_data_query,
                            'start_time': dateStart,
                            'end_time': dateEnd,
                            'query_size_heart': len(heart_rate_data_query),
                            'query_size_temp': len(temperature_data_query),
                            'errors': errors,
                            'text': text}
                            )
                    else:
                        errors.append("Data result is more than 30. Please select a shorter interval")
        default_heart_rate = HeartRateDataForm().default_query(request.user)
        default_temperature = TemperatureDataForm().default_query(request.user)
        text = "default latest heart rate reading result"
        return render(
            request,
            "statistics.html",
            {'user': request.user,
            'errors': errors,
            'heart_rate_data_query': default_heart_rate,
            'temperature_data_query': default_temperature,
            'query_size_heart': len(default_heart_rate),
            'query_size_temp': len(default_temperature),
            'text': text}
            )




class HeartRateTemperatureApi(APIView):
    """docstring for HeartRateApi"""
    authenticate_classes = []
    permission_classes = []

    def get(self, request, format = None):

        heart_rate_data = []
        hrate_date_recorded = []
        temperature_data = []
        temp_date_recorded = []

        for item in request.user.heartratedata_set.order_by('-time_recorded').order_by('time_recorded')[:10]:
            heart_rate_data.append(item.heart_rate_reading)
            hrate_date_recorded.append(item.time_recorded.strftime('%d/%m/%Y %H:%M'))

        for item in request.user.temperaturedata_set.order_by('-time_recorded').order_by('time_recorded')[:10]:
            temperature_data.append(item.temperature_reading)
            temp_date_recorded.append(item.time_recorded.strftime('%d/%m/%Y %H:%M'))

        data = {
            "heart_rate_data": heart_rate_data,
            "hrate_date_recorded": hrate_date_recorded,
            "temperature_data": temperature_data,
            "temp_date_recorded": temp_date_recorded,
        }
        return Response(data)


def home(request):
    return render(request, "home.html", {'user': request.user})


def refresh(request):
    return render(request, "reading.html")


def logout_user(request):
    logout(request)
    return redirect('HealthMonitoring:home')


def link_redirect(request):
    return redirect('HealthMonitoring:home')


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("HealthMonitoring:login_user")
        else:
            form = RegistrationForm()
            return render(request, "register_form.html", {'form': form})
    else:
        form = RegistrationForm()
        return render(request, "register_form.html", {'form': form})


def create_profile_from_device(self, username, email, password, firstname, lastname, middlename, birthday, age, gender, cellphone_number):
    
    created_user = User.objects.create_user(username, email, password)
    created_user.first_name = firstname
    created_user.last_name = lastname
    created_user.save()

    created_user_profile = Profile(
            user = created_user,
            middle_name = middlename,
            birthday = birthday,
            age = age,
            gender = gender,
            cellphone_number = cellphone_number,
        )
    created_user_profile.save()

    return HttpResponse("successful!")

def save_heart_rate_from_device(self, user, reading, status):

    user_get = User.objects.get(username = user)

    save_data = HeartRateData(
            data_from_user = user_get,
            heart_rate_reading = reading,
            status = status,
        )
    save_data.save()
    return HttpResponse("successful!")
    

def save_temp_from_device(self, user, reading, status):

    user_get = User.objects.get(username = user)

    save_data = TemperatureData(
            data_from_user = user_get,
            temperature_reading = reading,
            status = status,
        )
    save_data.save()
    return HttpResponse("successful!")