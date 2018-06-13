from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D
from django.conf import settings

from rest_framework import serializers
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

from .models import Profile


class ShowProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profile
		fields = ('id','last_name','first_name','password')

