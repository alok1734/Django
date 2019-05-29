from django.shortcuts import render
from rest_framework import viewsets
from serializers import UserRegistrationSerializer
from models import User

class UserRegistrationViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserRegistrationSerializer