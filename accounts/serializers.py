from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate
import json
from django.views.decorators.csrf import csrf_exempt
from . models import *

from rest_framework import serializers
from accounts.models import *
from django.contrib.auth import authenticate
from rest_framework import serializers
import logging
# Create your views here.


# Common Login Serializers for Librarian,SuperUser and officeStaff

logger = logging.getLogger(__name__)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = User.objects.get(email=email)
            logger.debug(f"Found user by email: {user.email}")
        except User.DoesNotExist:
            raise serializers.ValidationError("No account found with this email.")

        # Check user role
        if not (user.is_librarian or user.is_office_staff or user.is_superuser or user.is_staff):
            raise serializers.ValidationError('This account is not registered under a recognized role.')
  # Verify password
        if not user.check_password(password):
            logger.debug(f"Password verification failed for user: {user.full_name}")
            raise serializers.ValidationError('Invalid password.')
        
        logger.debug("Authentication successful.")
        attrs['user'] = user
        return attrs
    