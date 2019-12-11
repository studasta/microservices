from django import forms
from . import models

class CreateUser(forms.ModelForm):
	class Meta:
		model = models.User
		fields = ['first_name', 'last_name', 'address', 'role', 'login', 'password']