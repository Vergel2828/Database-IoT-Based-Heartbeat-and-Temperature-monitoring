from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin
from .models import Profile, HeartRateData, TemperatureData

class ProfileAdmin(admin.ModelAdmin):
	model = Profile


class HeartRateDataAdmin(admin.ModelAdmin):
	model = HeartRateData


class TemperatureDataAdmin(admin.ModelAdmin):
	model = TemperatureData


admin.site.register(Profile, ProfileAdmin)
admin.site.register(HeartRateData, HeartRateDataAdmin)
admin.site.register(TemperatureData, TemperatureDataAdmin)
