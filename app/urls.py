from django.urls import path, include 
from . import views

urlpatterns = [
	path('auth/', include('app.route.auth')),
    path('', views.index)
]