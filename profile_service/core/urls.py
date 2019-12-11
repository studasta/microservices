from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
	path('profile/', views.login_view, name='login')
]