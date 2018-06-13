from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from HealthMonitoring.models import HeartRateData, TemperatureData


class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=150, widget = forms.TextInput(
		attrs = {
			"class": 'form-control input-lg',
			"placeholder": 'Username'
		}
	))
	password = forms.CharField(label='Password',widget = forms.PasswordInput(
		attrs = {
			"class": 'form-control input-lg',
			"placeholder": 'Password'
		}
	))


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user


class HeartRateDataForm(forms.ModelForm):
	"""docstring for HeartRateDataForm"""

	class Meta:
		model = HeartRateData
		fields = "__all__"

	def query(self, date_start, date_end, user_login):
		result = HeartRateData.objects.all().filter(data_from_user=user_login).filter(time_recorded__range=(date_start, date_end)).order_by('-time_recorded').order_by('time_recorded')
		return result

	def default_query(self,user_login):
		result = HeartRateData.objects.all().filter(data_from_user=user_login).order_by('-time_recorded').order_by('time_recorded')[:25]
		return result

class TemperatureDataForm(forms.ModelForm):
	"""docstring for TemperatureDataForm"""
	
	class Meta:
		model = TemperatureData
		fields = "__all__"

	def query(self, date_start, date_end, user_login):
		result = TemperatureData.objects.all().filter(data_from_user=user_login).filter(time_recorded__range=(date_start, date_end)).order_by('-time_recorded').order_by('time_recorded')
		return result

	def default_query(self,user_login):
		result = TemperatureData.objects.all().filter(data_from_user=user_login).order_by('-time_recorded').order_by('time_recorded')[:25]
		return result
	
		

		
