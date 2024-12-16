from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from accounts.models import*
from .serializers import*
from rest_framework import generics
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from rest_framework.permissions import AllowAny
# Create your views here.


#Common Login View
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        # Look up the user by email
        user = User.objects.filter(email=email).first()

        if user and user.check_password(password):
            user_role = None
            custom_id = None
 # Determine user role and fetch custom_id
            if user.is_librarian:
                user_role = 'Librarian'
                custom_id = user.librarian.get().custom_id
            elif user.is_office_staff:
                user_role = 'Office staff'
                custom_id = user.office_staff.get().custom_id            
            elif user.is_superuser:
                user_role = 'Superuser'
            elif user.is_staff:
                user_role = 'Staff'
            else:
                return Response({'detail': 'User role not recognized.'}, status=status.HTTP_403_FORBIDDEN)
        
            # Create JWT token
            refresh = RefreshToken.for_user(user)
            update_last_login(None, user)

            logger.info(f"User {user.email} logged in successfully with role: {user_role}")
            return Response({
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
                'user_id': user.id,
                'email': user.email,
                'full_name': user.full_name,
                'user_type': user_role,
                'custom_id': custom_id,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)