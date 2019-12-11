from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from . import forms

def login_view(request):
	return HttpResponse("Login view.")

def singup_view(request):
	if request.method == 'POST':
		form = forms.CreateUser(request.POST, request.FILES)
		if form.is_valid():
			form.save()

def get(self, request):
	return Response("okkk")