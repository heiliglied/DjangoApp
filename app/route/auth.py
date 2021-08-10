from django.urls import path
from app.views import auth

urlpatterns = [
	path('login', auth.login),
]