from django.shortcuts import render
from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import (
										password_reset,
										password_reset_done,
										password_reset_confirm,
										password_reset_complete,
									)
from django.views.generic import ListView, DetailView, TemplateView

urlpatterns = [
		url(r'^$', views.link_redirect),
		url(r'^home/$', views.home, name='home'),
		url(r'^refresh/$', views.refresh, name='refresh'),
		url(r'^login/$', views.login_user, name='login_user'),
		url(r'^register/$', views.register_user, name='register'),
		url(r'^statistics/$', views.Statistics.as_view(), name='statistics'),
		url(r'^logout/$', views.logout_user, name='logout_user'),
		url(r'^heart-temp/data/api/$', views.HeartRateTemperatureApi.as_view(), name='heart_temp_data_api'),
		
		url(r'^reset-password/$', password_reset, {'post_reset_redirect':
			'HealthMonitoring:password_reset_done', 'email_template_name':
			'reset_password_email.html'}, name='reset_password'),
		url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
		
		url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
			password_reset_confirm, {'post_reset_redirect':
			'HealthMonitoring:password_reset_complete'}, name='password_reset_confirm'),
		
		url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),

		url(r'^create/device/(?P<username>[\w|\W]+)/(?P<email>[\w|\W.@+-|\d]+)/(?P<password>[\w|\W.@+-|\d]+)/(?P<firstname>[\w|\W]+)/(?P<lastname>[\w|\W]+)/(?P<middlename>[\w|\W]+)/(?P<birthday>\d{4}-\d{2}-\d{2})/(?P<age>\d+)/(?P<gender>[\w]+)/(?P<cellphone_number>\d+)/$',
			views.create_profile_from_device, name="profile_created"),
		#http://localhost:8000/create/device/testuser1/testuser1@gmail.com/passwordtestuser1/testuserf/testuserl/testuserm/1997-02-02/21/M/09101899132
		
		url(r'^create/device/save/heart/(?P<user>[\w|\W]+)/(?P<reading>\d+)/(?P<status>[\w|\W]+)/$',
			views.save_heart_rate_from_device, name='save_hrate_data'),
		#http://localhost:8000/create/device/save/heart/guest/60/EB/

		url(r'create/device/save/temp/(?P<user>[\w|\W]+)/(?P<reading>\d{2}.\d{2})/(?P<status>[\w|\W]+)/$',
			views.save_temp_from_device, name='save_temp_data'),
		#http://localhost:8000/create/device/save/temp/guest/37.50/FE/
	]